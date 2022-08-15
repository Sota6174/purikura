import cv2
import numpy as np
from moviepy.editor import TextClip, ImageClip, CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from settings import CASCADE_PATH, FONT, SMASH_VIDEO_PATH, FONT_SIZE


def generate(image: np.ndarray, user_name: str) -> CompositeVideoClip:
    """スマブラの参戦ムービー風動画を生成する

    Args:
        image (np.ndarray): 参戦者画像
        user_name (str): 参戦者名

    Returns:
        CompositeVideoClip: 生成動画のclip
    """
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 2)

    for (x, y, w, h) in faces:
        hh = int(h / 2.8)
        ww = int(w / 1.5)
        image = image[y - hh : y + h * 2, x - ww : x + w + ww]
        break

    image = cv2.resize(image, dsize=(1215, 1200))

    fontsize = int(FONT_SIZE)
    if len(user_name) > 4:
        fontsize = 1000 / len(user_name)

    clip = VideoFileClip(SMASH_VIDEO_PATH)
    textclip1 = (
        TextClip(
            txt=f"{user_name}",
            color="whitesmoke",
            font=FONT,
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
            font=FONT,
            stroke_color="black",
            fontsize=280,
            stroke_width=8,
            size=(clip.w, clip.h),
        )
        .set_position((-500, 60))
        .set_start(6.5)
        .rotate(4)
    )

    imageclip = ImageClip(cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)).set_position((800, -100)).set_start(6.5)

    cvc = CompositeVideoClip([clip, textclip1, textclip2, imageclip])

    clip = cvc.set_duration(clip.duration)

    return clip
