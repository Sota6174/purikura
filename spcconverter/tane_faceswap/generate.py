import cv2
from ..utils.remove_gb import clip_background
from ..utils.call_inf_server import call_inf_server
from ..utils.super_resolution import super_resolution


def generate(src_image, output_path: str):
    print(f"[{__name__}]start")
    image = clip_background(src_image)
    image = call_inf_server("faceswap", image)
    print(f"[{__name__}]end")
    cv2.imwrite(output_path, image)
