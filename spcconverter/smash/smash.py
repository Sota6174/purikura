import glob
import os.path as op
import cv2
import numpy as np
from moviepy.editor import TextClip, ImageClip, CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import pkg_resources

from ..utils.remove_gb import remove_green_chromakey


def generate(img, usr_name, output_path, fontsize=280):
    """
    img: remove_green_chromakey()から渡される画像
    usr_name: 参戦させるユーザーの名前
    output_path: 保存するpath
    fontsize: 表示させるユーザーの名前のサイズ。５文字以上だと自動的に小さくなる
    cascade_path: 画像認識モデルのpath
    font: fontのpath
    smash_video_path: 元動画のpath
    """
    cascade_path = pkg_resources.resource_filename(
        "spcconverter", "assets/smash/haarcascade_frontalface_alt.xml"
    )
    font = pkg_resources.resource_filename(
        "spcconverter", "assets/smash/GenShinGothic-Bold.ttf"
    )
    smash_video_path = pkg_resources.resource_filename(
        "spcconverter", "assets/smash/smash-pre.mp4"
    )

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
    generate(img=img, usr_name=usr_name, output_path=output_path)
