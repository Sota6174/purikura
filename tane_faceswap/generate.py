import cv2
import numpy as np
import urllib.parse
import urllib.request
import tempfile
from settings import FACESWAP_INF_SERVER_URL


def generate(image: np.ndarray) -> np.ndarray:
    """画像の顔を種市さんの顔と合成した画像を生成する

    Args:
        image (np.ndarray): 入力画像

    Returns:
        np.ndarray: 生成画像
    """
    url = FACESWAP_INF_SERVER_URL
    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        dump_path = f.name
        cv2.imwrite(dump_path, image)
        f.seek(0)
        body = f.read()

    req = urllib.request.Request(url, body, method="POST", headers={"Content-Type": "application/octet-stream"})

    with urllib.request.urlopen(req) as res:
        swapped_image = res.read()
        with tempfile.NamedTemporaryFile(suffix=".png") as f:
            f.write(swapped_image)
            f.seek(0)
            out_data = cv2.imread(f.name)

    return out_data
