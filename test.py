import os

os.environ["INPUT_IMAGE_DIR"] = "."
os.environ["OUTPUT_IMAGE_DIR"] = "./output_images"

import spcconverter as spc

if __name__ == "__main__":
    img_path = "./spcconverter/assets/kiminonaha/dummy.jpg"
    out_path = spc.convert([img_path], 0, "")
    print(out_path)
    out_path = spc.convert([img_path], 1, "")
    print(out_path)
    out_path = spc.convert([img_path], 2, "")
    print(out_path)
