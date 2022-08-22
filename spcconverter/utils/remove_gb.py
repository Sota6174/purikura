import cv2
import numpy as np
import glob


def surround_with_green(path: str) -> np.ndarray:
    up, down, left, right = 0.15, 0.08, 0.30, 0.30

    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    h, w = image.shape[:2]
    for y in range(0, h):
        for x in range(0, w):
            if (h * up > y) or (y > h * (1 - down)) or (w * left > x) or (x > w * (1 - right)):
                image[y, x] = [0, 255, 0]

    return image


def remove_green_hsv(path: str) -> np.ndarray:
    # グリーンバック以外の背景をグリーンバックにする
    image = surround_with_green(path)

    # hsvに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # hsv色空間でマスキング画像生成
    lower = np.array([55, 64, 30])
    upper = np.array([75, 255, 255])
    mask_image = cv2.inRange(image, lower, upper)  # マスキング処理（緑色を255、緑色以外を0にした画像を生成する）

    # BGRA色空間でマスク部分削除
    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    image = cv2.bitwise_not(image, image, mask=mask_image)  # 元画像とマスク画像の演算（マスク部分削除）

    return image


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


if __name__ == "__main__":
    for path in glob.glob("images/*.png"):
        print(path)
        remove_green_hsv(path)
        remove_green_chromakey(path)
