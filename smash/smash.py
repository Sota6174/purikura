import glob
import os.path as op

import cv2
import numpy as np
from moviepy.editor import TextClip, ImageClip, CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def remove_green_chromakey(path: str):
    norm_factor = 255
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if image.ndim == 3:  # RGBならアルファチャンネル追加
        image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
    # print(image.shape)  # (h, w, 4)

    # 画素の最大輝度値255で各チャンネルの値を正規化
    red_ratio = image[:, :, 0] / norm_factor
    green_ratio = image[:, :, 1] / norm_factor
    blue_ratio = image[:, :, 2] / norm_factor

    # 赤(青) - 緑の値が0以下のとき、そのピクセルは緑色である可能性が高い
    # 赤(青)も緑も値が小さい（暗い色の）場合まで緑判定しないように0.3を先に足す
    red_vs_green = (red_ratio - green_ratio) + 0.3
    blue_vs_green = (blue_ratio - green_ratio) + 0.3
    red_vs_green[red_vs_green < 0] = 0
    blue_vs_green[blue_vs_green < 0] = 0

    # alpha値を算出する（輝度値が大きいほどalpha値も大きい）
    alpha = (red_vs_green + blue_vs_green) * 255
    alpha[alpha > 50] = 255
    image[:, :, 3] = alpha

    return image


def smash(img, usr_name, output_path, fontsize=280):
    """
    img: remove_green_chromakey()から渡される画像
    usr_name: 参戦させるユーザーの名前
    output_path: 保存するpath
    fontsize: 表示させるユーザーの名前のサイズ。５文字以上だと自動的に小さくなる
    cascade_path: 画像認識モデルのpath
    font: fontのpath
    smash_video_path: 元動画のpath
    """
    cascade_path = "./haarcascade_frontalface_alt.xml"
    font = "./GenShinGothic-Bold.ttf"
    smash_video_path = "./smash-pre.mp4"

    face_cascade = cv2.CascadeClassifier(cascade_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 2)

    for (x, y, w, h) in faces:
        hh = int(h / 2.8)
        ww = int(w / 1.5)
        img = img[y - hh : y + h * 2, x - ww : x + w + ww]
        break

    img = cv2.resize(img, dsize=(1215, 1200))

    if len(usr_name) > 4:
        fontsize = 1000 / len(usr_name)

    clip = VideoFileClip(smash_video_path)
    textclip1 = (
        TextClip(
            txt=f"{usr_name}",
            color="whitesmoke",
            font=font,
            stroke_color="black",
            fontsize=fontsize,
            stroke_width=8,
            size=(clip.w, clip.h),
        )
        .set_position((-500, -200))
        .set_start(6.5)
        .rotate(4)
    )
    textclip2 = (
        TextClip(
            txt="参戦!!",
            color="yellow",
            font=font,
            stroke_color="black",
            fontsize=280,
            stroke_width=8,
            size=(clip.w, clip.h),
        )
        .set_position((-500, 60))
        .set_start(6.5)
        .rotate(4)
    )

    imageclip = (
        ImageClip(cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA))
        .set_position((800, -100))
        .set_start(6.5)
    )

    cvc = CompositeVideoClip([clip, textclip1, textclip2, imageclip])

    clip = cvc.set_duration(clip.duration)
    clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
    )


if __name__ == "__main__":
    file_path = "./test.png"
    usr_name = "Name"
    output_path = "./test.mp4"

    img = remove_green_chromakey(file_path)
    smash(img=img, usr_name=usr_name, output_path=output_path)
