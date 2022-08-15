import os
import sys
from remove_gb import remove_green_hsv, remove_green_chromakey
import cv2
import settings
import tane_faceswap

os.makedirs(settings.OUTPUT_IMAGE_DIR, exist_ok=True)

if __name__ == "__main__":
    _, id, *path_list = sys.argv
    # print(id, path_list)

    output_path_list = []
    for path in path_list:
        # image = remove_green_hsv(path)
        image = remove_green_chromakey(path)

        if id == "0":
            pass
        elif id == "1":
            image = tane_faceswap.generate(image)
        elif id == "2":
            pass

        # 画像保存
        file_name = os.path.basename(path)
        output_path = os.path.join(settings.OUTPUT_IMAGE_DIR, file_name)
        cv2.imwrite(output_path, image)
        output_path_list.append(output_path)
    print(output_path_list)
