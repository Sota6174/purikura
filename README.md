## purikura

### 環境構築：.envファイルの編集
1. `OUTPUT_IMAGE_DIR`の指定
* 指定がない場合は、デフォルト値として`"output_images"`が指定される
* `OUTPUT_IMAGE_DIR`で指定されているディレクトリが存在しない場合は、作成される

例
```.env
OUTPUT_IMAGE_DIR=output_images
```

### 実行方法
* 画像１枚を入力する場合  
`$ py main.py <テンプレート番号> <入力画像パス>`

* 画像２枚を入力する場合  
`$ py main.py <テンプレート番号> <入力画像パス１> <入力画像パス２>`

### tane_faceswapの使い方

1. 別で作成した[推論用サーバーノートブック](https://colab.research.google.com/drive/1DWNkqhWsqCuLOrphlcC0FhH6ttsFLoHu?usp=sharing)を実行
2. 発行された URL を 環境変数 FACESWAP_INF_SERVER_URL に記載
3. generate 関数を呼び出す
