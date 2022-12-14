import os

os.environ["INPUT_IMAGE_DIR"] = "."
os.environ["OUTPUT_IMAGE_DIR"] = "./output_images"

import spcconverter as spc
import glob

if __name__ == "__main__":
    # jpg → png変換用
    # path_list = glob.glob("./images/*.jpg")
    # print(len(path_list))
    # print(path_list)
    # for path in path_list:
    #     Image.open(path).save(path.replace(".jpg", ".png"))

    img_path = "./images/8b36d7d9-f2bb-459b-9b85-f6c44829a84c.png"
    out_path = spc.convert([img_path], 0, "")
    print(out_path)
    out_path = spc.convert([img_path], 1, "")
    print(out_path)
    out_path = spc.convert([img_path], 2, "")
    print(out_path)

    path_list = [path.split("\\")[-1] for path in glob.glob("images/*.png")]
    print(path_list)  # ファイル名だけのリストになっているか確認
    out_path_list = spc.convert_all(path_list)
    print(out_path_list)
