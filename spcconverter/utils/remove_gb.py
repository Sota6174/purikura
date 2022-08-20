import cv2
import numpy as np
import glob


def remove_green_hsv(path: str) -> np.ndarray:
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # (h, w, 3)

    # hsvに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # hsv色空間でマスキング処理
    lower = np.array([30, 64, 0])
    upper = np.array([90, 255, 255])
    mask_image = cv2.inRange(image, lower, upper)  # マスキング処理（緑色を255、緑色以外を0にした画像を生成する）
    image = cv2.bitwise_not(image, image, mask=mask_image)  # 元画像とマスク画像の演算（マスク部分削除）

    # bgra色空間に戻す
    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # 背景が黒[0, 0, 0, 255]になっている箇所を透過色[255, 255, 255, 0]に変更する
    mask_image = cv2.inRange(image, np.array([0, 0, 0, 255]), np.array([0, 0, 0, 255]))
    image = cv2.bitwise_not(image, image, mask=mask_image)

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
