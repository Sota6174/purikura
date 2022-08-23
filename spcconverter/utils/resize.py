import cv2
from dotenv import load_dotenv
import os

# 画像を開く
load_dotenv()
BACKGROUND_IMAGE_PATH = os.getenv("BACKGROUND_IMAGE_PATH")
image = cv2.imread(BACKGROUND_IMAGE_PATH, cv2.IMREAD_UNCHANGED)
print(image.shape[:2])

# resize
image = cv2.resize(image, dsize=(640, 480))

# 切り抜いた画像の保存
BACKGROUND_IMAGE_PATH = BACKGROUND_IMAGE_PATH.replace("1.png", "3.png")
print(BACKGROUND_IMAGE_PATH)
cv2.imwrite(BACKGROUND_IMAGE_PATH, image)
