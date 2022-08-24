import cv2
from dotenv import load_dotenv
import os
import glob

load_dotenv()
BACKGROUND_IMAGE_PATH = os.getenv("BACKGROUND_IMAGE_PATH")

# 画質一括確認
path = BACKGROUND_IMAGE_PATH.replace(BACKGROUND_IMAGE_PATH.split("\\")[-1], "")
path_list = glob.glob(f"{path}*.png")
print(path_list)
for path in path_list:
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    print(path.split("\\")[-1] + f": (width, height) = {image.shape[:2][::-1]}")

# 画像を開く
image = cv2.imread(BACKGROUND_IMAGE_PATH, cv2.IMREAD_UNCHANGED)
print(image.shape[:2][::-1])  # (width, height)

# resize
image = cv2.resize(image, dsize=(1440, 1080))  # dsize=(width, height)

# 切り抜いた画像の保存
BACKGROUND_IMAGE_PATH = BACKGROUND_IMAGE_PATH.replace("620_536.png", "1440_1080.png")
print(BACKGROUND_IMAGE_PATH)
cv2.imwrite(BACKGROUND_IMAGE_PATH, image)
