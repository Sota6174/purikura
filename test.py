import os
import spcconverter as spc
import glob

os.environ["INPUT_IMAGE_DIR"] = "."
os.environ["OUTPUT_IMAGE_DIR"] = "./output_images"

if __name__ == "__main__":
    # jpg → png変換用
    # path_list = glob.glob("./images/*.jpg")
    # print(len(path_list))
    # print(path_list)
    # for path in path_list:
    #     Image.open(path).save(path.replace(".jpg", ".png"))

    img_path = "./spcconverter/assets/kiminonaha/dummy.jpg"
    out_path = spc.convert([img_path], 0, "")
    print(out_path)
    out_path = spc.convert([img_path], 1, "")
    print(out_path)
    out_path = spc.convert([img_path], 2, "")
    print(out_path)

    path_list = [path.split("//")[-1] for path in glob.glob("./images/*.png")]
    out_path_list = spc.convert_all(path_list)
    print(out_path_list)
