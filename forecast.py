import csv
import numpy as np
import tensorflow as tf
import keras
from PIL import Image
from tensorflow.python.keras.models import load_model

#風向を数値に変換する
dirs = ['北', '北北東', '北東', '東北東', '東', '東南東', '南東', '南南東', '南', '南南西', '南西', '西南西', '西', '西北西', '北西', '北北西', '']
def dir_to_num(s):
    return dirs.index(s)

#天気を数値に変換する
#雲量・降水量のデータもあるため、その日の「メイン」の天気だけあれば良いでしょう
def weather_to_num(s):
    match s[0]:
        case '快':
            return 1
        case '晴':
            return 2
        case '薄':
            return 3
        case '曇':
            return 4
        case '煙':
            return 5
        case '砂':
            return 6
        case '地':
            return 7
        case '霧':
            if len(s)>=2 and s[1]=='雨':
                return 9
            else:
                return 8
        case '雨':
            return 10
        case 'み':
            return 11
        case '雪':
            return 12
        case 'あ':
            return 13
        case 'ひ':
            return 14
        case '雷':
            return 15
        case _:
            return 0

with open(input("path/to/csv:"), 'r', encoding="Shift-JIS") as f:
    read = csv.reader(f)
    l = [row for row in read]
    place = l[2]
    data_name = l[3]
    data = [l[6], l[7], l[8]]

x = []

for toshi in ["東京", "名古屋", "大阪", "新潟", "仙台", "鹿児島", "銚子", "熊谷", "甲府", "横浜"]:
    for day in range(3):
        s = place.index(toshi)
        t = s
        while t < len(place) and place[t] == toshi:
            t += 1
        for now in ['降水量の合計(mm)','最高気温(℃)','最低気温(℃)','最多風向(16方位)','天気概況(昼：06時〜18時)','平均雲量(10分比)','平均蒸気圧(hPa)']:
            if now == '平均雲量(10分比)' and toshi in ["銚子", "熊谷", "甲府", "横浜"]:
                continue
            idx = data_name.index(now, s,t)
            val = data[day][idx]
            if now == '最多風向(16方位)':
                val = dir_to_num(val)
            elif now == '天気概況(昼：06時〜18時)':
                val = weather_to_num(val)
            else:
                val = float(val)
            x.append(val)

model = keras.models.load_model(input("path/to/model:"))
img_chart = Image.open(input("path/to/天気図:"))
chart = np.array(img_chart.resize((600, 450)))/255
img_rader = Image.open(input("path/to/雨雲レーダー:"))
rader = np.array(img_rader.resize((692, 520)))/255

print(model.predict([np.array([x]),np.array([chart]),np.array([rader])]))