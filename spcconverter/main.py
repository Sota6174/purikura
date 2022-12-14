import os
import sys
from typing import List
import uuid
import pkg_resources
import random

from . import smash
from . import kiminonaha
from .utils.remove_gb import remove_green_hsv
from . import settings
from . import tane_faceswap


def convert(path_list: List[str], template_id: int, username: str = ""):
    os.makedirs(settings.OUTPUT_IMAGE_DIR, exist_ok=True)
    dummy_img_path = pkg_resources.resource_filename(
        "spcconverter", "assets/kiminonaha/dummy.jpg"
    )

    def load_and_hsv(path):
        path = os.path.join(settings.INPUT_DIR, path)
        image = remove_green_hsv(path)
        return image

    images = [load_and_hsv(path) for path in [path_list[0], dummy_img_path]]

    def get_output_path(suffix):
        file_name = str(uuid.uuid4()) + suffix
        output_path = os.path.join(settings.OUTPUT_IMAGE_DIR, file_name)
        return output_path

    if template_id == 0:
        output_path = get_output_path(".mp4")
        if username == "":
            username = "†名もなきアンノウン†"
        smash.generate(img=images[0], usr_name=username, output_path=output_path)
        pass
    elif template_id == 1:
        output_path = get_output_path(".png")
        tane_faceswap.generate(src_image=images[0], output_path=output_path)
    elif template_id == 2:
        output_path = get_output_path(".png")
        kiminonaha.generate(image1=images[0], image2=images[1], output_path=output_path)

    return output_path


def convert_all(path_list: List[str]):
    os.makedirs(settings.OUTPUT_IMAGE_DIR, exist_ok=True)
    output_path_list = []

    def load_and_hsv(path):
        path = os.path.join(settings.INPUT_DIR, path)
        image = remove_green_hsv(path)
        return image

    def get_output_path(suffix):
        file_name = str(uuid.uuid4()) + suffix
        output_path = os.path.join(settings.OUTPUT_IMAGE_DIR, file_name)
        return output_path

    if len(path_list) % 2 != 0:
        path_list.append(
            pkg_resources.resource_filename(
                "spcconverter", "assets/kiminonaha/dummy.jpg"
            )
        )

    random_index_list = random.sample(range(len(path_list)), len(path_list))
    it = iter(random_index_list)
    for idx1, idx2 in zip(it, it):
        image1 = load_and_hsv(path_list[idx1])
        image2 = load_and_hsv(path_list[idx2])
        output_path = get_output_path(".png")
        kiminonaha.generate(image1=image1, image2=image2, output_path=output_path)
        output_path_list.append(output_path)

    return output_path_list


if __name__ == "__main__":
    _, id, path_list = sys.argv
    id = int(id)
    out_paths = convert(path_list=path_list, template_id=id)
    print(out_paths)
