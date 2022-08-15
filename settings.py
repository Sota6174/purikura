import os
from dotenv import load_dotenv

load_dotenv()

# 出力画像の保存先ディレクトリの設定
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "unspecified")

# smashの設定
CASCADE_PATH = os.environ.get("CASCADE_PATH", "unspecified")  # 画像認識モデルのpath
FONT = os.environ.get("FONT", "unspecified")  # fontのpath
SMASH_VIDEO_PATH = os.environ.get("SMASH_VIDEO_PATH", "unspecified")  # 元動画のpath
FONT_SIZE = os.environ.get("FONT_SIZE", "unspecified")  # fontの大きさ

# tane_faceswapの設定
FACESWAP_INF_SERVER_URL = os.environ.get("FACESWAP_INF_SERVER_URL", "unspecified")

# kiminonahaの設定
BACKGROUND_IMAGE_PATH = os.environ.get("BACKGROUND_IMAGE_PATH", "unspecified")
FOOT_HEIGHT = 16 if "1" in BACKGROUND_IMAGE_PATH else 64  # 背景画像との合成時の足の高さ
