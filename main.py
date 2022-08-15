from importlib.resources import path
import os
import sys
from typing import List
from remove_gb import remove_green_chromakey
import cv2
import settings
import tane_faceswap


def convert(path_list: List[str], template_id: int):
    os.makedirs(settings.OUTPUT_IMAGE_DIR, exist_ok=True)

    output_path_list = []
    for path in path_list:
        image = remove_green_chromakey(path)

        if template_id == "0":
            pass
        elif template_id == "1":
            image = tane_faceswap.generate(image)
        elif template_id == "2":
            pass

        # 画像保存
        file_name = os.path.basename(path)
        output_path = os.path.join(settings.OUTPUT_IMAGE_DIR, file_name)
        cv2.imwrite(output_path, image)
        output_path_list.append(output_path)
    return output_path_list


if __name__ == "__main__":
    _, id, path_list = sys.argv
    out_paths = convert(path_list=path_list, template_id=id)
    print(out_paths)
