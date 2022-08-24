import cv2
import urllib.parse
import urllib.request
import tempfile
from .. import settings


def call_inf_server(endpoint, image):
    print(f"[{__name__}]start endpoint={endpoint}")
    url = urllib.parse.urljoin(settings.INF_SERVER_URL, endpoint)

    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        dump_path = f.name
        cv2.imwrite(dump_path, image)
        f.seek(0)
        body = f.read()

    print(f"[{__name__}]send request to {str(url)}")
    req = urllib.request.Request(
        url, body, method="POST", headers={"Content-Type": "application/octet-stream"}
    )

    with urllib.request.urlopen(req) as res:
        print(f"[{__name__}]succeed")
        img_bytes = res.read()
        with tempfile.NamedTemporaryFile(suffix=".png") as f:
            f.write(img_bytes)
            result_image = cv2.imread(f.name)
    print(f"[{__name__}]end")
    return result_image
