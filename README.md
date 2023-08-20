# inf_alpha

情報 α 期末課題．  

## learn.ipynb
学習に用いたコード．  
rundir を適当にデータセットのある場所へのパスに書き換えれば動作する．  
（実際には 1500 件弱のデータを用いたが，現在フォルダ dataset には 50 件ほどしか入っていない．）

## my_model.h5
最終的に学習を終えたモデル．

## dataset
実際に使用したデータセットの一部．

## forecast.py
これを実行することで気象予測ができる．以降，天気を予測したい日付を d 日とする  
  
### step 1.  
気象庁のページ https://www.data.jma.go.jp/risk/obsdl/index.php から，東京，名古屋，大阪，新潟，仙台，鹿児島，銚子，熊谷，甲府，横浜における，降水量の合計(mm)，最高気温(℃)，最低気温(℃)，最多風向(16方位)，天気概況(昼：06時〜18時)，平均雲量(10分比)，平均蒸気圧(hPa)の， d-3 日から d-1 日のデータを csv ファイルとしてダウンロードする．  
例として， 2023/08/17 ~ 2023/08/19 のデータをダウンロードした csv ファイルが dataset/20230817_0819.csv に置いてある．  
  
### step 2.  
日本気象協会のページ https://tenki.jp/past/2023/08/19/radar/, https://tenki.jp/past/2023/08/19/chart/ から， d-1 日の 18 時時点での雨雲レーダー，天気図の画像をダウンロードする（15 時などのデータを使ってもそれほど問題ないと思われる）．  
例として，2023/08/19 の画像をダウンロードした jpg ファイルが rader_2023081918.jpg,chart_2023081918.jpg に置いてある．  
  
### step 3.  
forecast.py を実行し，指示の通りモデルやデータへの path を入力する．  
[晴れ，雨，曇り，その他] となる確率を予測したベクトルが出力されるので，読む．  
  
以下は，2023/08/20 の天気を予測した結果である．この日は都内は曇りであったので，正しく予測できている．  
<img width="632" alt="スクリーンショット 2023-08-20 23 04 41" src="https://github.com/mitsu-a/inf_alpha/assets/88711918/5dbce3af-1a9d-43a6-93e9-770f6401bda8">
