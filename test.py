import os
import spcconverter as spc
import glob

os.environ["INPUT_IMAGE_DIR"] = "."
os.environ["OUTPUT_IMAGE_DIR"] = "./output_images"

if __name__ == "__main__":
    img_path = "./spcconverter/assets/kiminonaha/dummy.jpg"
    out_path = spc.convert([img_path], 0, "")
    print(out_path)
    out_path = spc.convert([img_path], 1, "")
    print(out_path)
    out_path = spc.convert([img_path], 2, "")
    print(out_path)

    path_list = [path.split("\\")[-1] for path in glob.glob("./images/*.png")]
    out_path_list = spc.convert_all(path_list)
    print(out_path_list)
