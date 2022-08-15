import cv2
import urllib.parse
import urllib.request
import tempfile
from .. import settings


def generate(img):
    url = settings.FACESWAP_INF_SERVER_URL

    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        dump_path = f.name
        cv2.imwrite(dump_path, img)
        f.seek(0)
        body = f.read()

    req = urllib.request.Request(
        url, body, method="POST", headers={"Content-Type": "application/octet-stream"}
    )

    with urllib.request.urlopen(req) as res:
        swapped_img = res.read()
        with tempfile.NamedTemporaryFile(suffix=".png") as f:
            f.write(swapped_img)
            f.seek(0)
            out_data = cv2.imread(f.name)

    return out_data
