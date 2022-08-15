## purikura

### 環境構築：.envファイルの編集
1. `OUTPUT_IMAGE_DIR`の指定
* 指定がない場合は、デフォルト値として`"output_images"`が指定される
* `OUTPUT_IMAGE_DIR`で指定されているディレクトリが存在しない場合は、作成される

例
```.env
OUTPUT_DIR=./output

CASCADE_PATH=./haarcascade_frontalface_alt.xml
FONT=./GenShinGothic-Bold.ttf
SMASH_VIDEO_PATH=./smash-pre.mp4
FONT_SIZE=200

FACESWAP_INF_SERVER_URL=<[推論用サーバーノートブック](https://colab.research.google.com/drive/1DWNkqhWsqCuLOrphlcC0FhH6ttsFLoHu?usp=sharing)の実行によって生成されるULRを記載>

BACKGROUND_IMAGE_PATH=<君の名はの背景画像パス>
```

### 実行方法
* スマブラの参戦ムービー風動画を生成する場合  
  `$ py main.py 0 <入力画像パス>`

* 画像の顔を種市さん（高橋さん）の顔と合成した画像を生成する場合  
  `$ py main.py 0 <入力画像パス>`

* 画像２枚を入力する場合  
  `$ py main.py <テンプレート番号> <入力画像パス１> <入力画像パス２>`