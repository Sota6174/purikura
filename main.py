import os
import sys
import cv2
from settings import OUTPUT_DIR
import smash
import tane_faceswap
import kiminonaha
from remove_gb import remove_green_chromakey

os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == "__main__":
    _, id, *path_list = sys.argv
    print(id, path_list)

    # グリーンバックを透明化
    images = [remove_green_chromakey(image) for image in path_list]
    print(images[0].shape)

    # 合成画像生成、保存
    file_name = "temp"  # path_listから生成できたらベスト

    if id == "0":  # smash
        user_name = "anonymous"  # file_nameかpath_listから生成できたらベスト
        clip = smash.generate(images[0], user_name)
        clip.write_videofile(
            f"{OUTPUT_DIR}/{file_name}.mp4",
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
        )
    elif id == "1":  # tane_faceswap
        image = tane_faceswap.generate(images[0])
        cv2.imwrite(f"{OUTPUT_DIR}/{file_name}.png", image)
    elif id == "2":  # kiminonaha
        image = kiminonaha.generate(images)
        cv2.imwrite(f"{OUTPUT_DIR}/{file_name}.png", image)
