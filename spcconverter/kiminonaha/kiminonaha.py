import cv2
import numpy as np
import pkg_resources
from ..utils.remove_gb import remove_green_chromakey


def resize_height_base(image: np.ndarray, height: int) -> np.ndarray:
    """画像の縦幅が指定した値になるようにリサイズ"""
    h, w = image.shape[:2]
    width = round((height / h) * w)

    return cv2.resize(image, dsize=(width, height))


def composite_image(background_image: np.ndarray, images: list, center: list) -> np.ndarray:
    """背景画像に画像を合成"""
    centers = [center, [center[0], center[1] * 3]]
    for i in range(2):
        image = images[i]
        center = centers[i]
        h, w = image.shape[:2]
        h1, h2, w1, w2 = (
            center[0] - h // 2,
            center[0] + h // 2,
            center[1] - w // 2,
            center[1] + w // 2,
        )
        if h % 2 == 1:
            h1 -= 1
        if w % 2 == 1:
            w1 -= 1
        for y in range(h1, h2):
            for x in range(w1, w2):
                if image[y - h1, x - w1, -1] != 0:  # alphaが0の部分だけ上書き
                    background_image[y, x] = image[y - h1, x - w1]

    return background_image


def generate(image1, image2, output_path) -> None:
    size = "1920_1440"
    BACKGROUND_IMAGE_PATH = pkg_resources.resource_filename("spcconverter", f"assets/kiminonaha/{size}.png")
    FOOT_HEIGHT = int(size.split("_")[-1]) // 15

    background_image = cv2.imread(BACKGROUND_IMAGE_PATH, cv2.IMREAD_UNCHANGED)
    bg_height, bg_width = background_image.shape[:2]

    height = bg_height // 2 - FOOT_HEIGHT
    center = ((bg_height + height) // 2, bg_width // 4)

    # 切り出し＋リサイズ（縦height基準）
    images = [resize_height_base(img, height) for img in [image1, image2]]

    # 2枚目の画像のみ左右反転
    images[-1] = cv2.flip(images[-1], 1)

    # 横幅が背景画像からはみ出ないようにトリミング
    if images[0].shape[1] // 2 > center[1]:
        trim = images[0].shape[1] // 2 - center[1]
        images = [image[:, trim:-trim] for image in images]

    # 画像を背景画像に合成
    image = composite_image(background_image, images, center)

    cv2.imwrite(output_path, image)
