import cv2
import os
import urllib.parse
import urllib.request
import uuid

dump_dir = "/tmp/purikura/dump"
if not os.path.exists(dump_dir):
    os.makedirs(dump_dir)
out_dir = "/tmp/purikura/out"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
url = "http://7671-34-90-166-18.ngrok.io"


def generate(img):
    dump_path = os.path.join(dump_dir, "dump.png")
    out_path = os.path.join(out_dir, str(uuid.uuid4()) + ".png")

    cv2.imwrite(dump_path, img)
    f = open(dump_path, "rb")
    body = f.read()
    f.close()
    req = urllib.request.Request(
        url, body, method="POST", headers={"Content-Type": "application/octet-stream"}
    )

    with urllib.request.urlopen(req) as res:
        print(res.info())
        swapped_img = res.read()
        with open(out_path, "wb") as f:
            f.write(swapped_img)

    print(out_path)
    return out_path


if __name__ == "__main__":
    data = cv2.imread("./testimg/sample.jpg")
    generate(data)
