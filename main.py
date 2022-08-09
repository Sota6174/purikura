from dotenv import load_dotenv
import os
import sys
from remove_gb import remove_green_hsv, remove_green_chromakey
import cv2

load_dotenv()
OUTPUT_IMAGE_DIR = os.environ.get("OUTPUT_IMAGE_DIR", "output_images")
os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)


if __name__ == "__main__":
    _, id, *path_list = sys.argv
    print(id, path_list)

    for path in path_list:
        # image = remove_green_hsv(path)
        image = remove_green_chromakey(path)

        # 画像保存
        file_name = path.split("\\")[-1]
        cv2.imwrite(f"{OUTPUT_IMAGE_DIR}/{file_name}", image)
