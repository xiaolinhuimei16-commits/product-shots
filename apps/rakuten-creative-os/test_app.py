"""Local smoke tests. Run: pip install httpx && python -m unittest discover -s apps/rakuten-creative-os -p 'test_*.py'"""
import io
import json
import sys
import unittest
import zipfile
from pathlib import Path

from fastapi.testclient import TestClient
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from app import app

def test_photo(color=(240, 200, 70)):
    image = Image.new("RGB", (240, 180), color)
    out = io.BytesIO()
    image.save(out, format="PNG")
    return out.getvalue()

def job(approved=True, label="バター風・単品"):
    manifest = {
        "skus":{"I":{"name":label}},
        "headlines":["商品画像 %02d" % n for n in range(1, 13)],
        "approved_ref_name":"employee-approved-reference",
        "approved_source":approved, "approved_copy":approved,
        "approved_style":approved, "reviewed_preview":approved,
        "background":"#fff4cf", "pink":"#f5a7b8", "brown":"#6d3a37"
    }
    return {
        "data":{"manifest":json.dumps(manifest, ensure_ascii=False)},
        "files":{"photo_I":("real-product.png", test_photo(), "image/png"),
                 "style_reference":("reference.png", test_photo(), "image/png")}
    }

class LocalWebMvpTest(unittest.TestCase):
    def test_homepage(self):
        with TestClient(app) as client:
            response=client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Rakuten Creative OS", response.text)

    def test_preview(self):
        with TestClient(app) as client:
            response=client.post("/api/preview", **job(False))
        self.assertEqual(response.status_code, 200, response.text[:500])
        im=Image.open(io.BytesIO(response.content))
        self.assertEqual(im.size, (1200, 900))

    def test_zip_has_twelve_independent_jpegs(self):
        with TestClient(app) as client:
            response=client.post("/api/export", **job())
        self.assertEqual(response.status_code, 200, response.text[:500] if response.status_code!=200 else "")
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            jpgs=sorted(name for name in z.namelist() if name.endswith(".jpg"))
            self.assertEqual(len(jpgs), 12)
            for name in jpgs:
                im=Image.open(io.BytesIO(z.read(name)))
                self.assertEqual(im.size, (1000, 1000))
            manifest=json.loads(z.read("QA_MANIFEST.json"))
            self.assertEqual(manifest["status"], "PENDING_HUMAN_FINAL_QA")

    def test_missing_approval_blocks_export(self):
        with TestClient(app) as client:
            response=client.post("/api/export", **job(False))
        self.assertEqual(response.status_code, 422)

    def test_no_invented_sku(self):
        payload=job()
        payload["files"]={"style_reference":("reference.png",test_photo(),"image/png")}
        with TestClient(app) as client:
            response=client.post("/api/export", **payload)
        self.assertEqual(response.status_code, 422)

if __name__ == "__main__":
    unittest.main()
