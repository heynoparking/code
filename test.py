import requests
import pandas as pd
import json

url = 'http://210.69.35.216/od/data/api/88C78BC3-DF8F-4FC6-9E22-F65648B6CFD1?$format=csv'

r = requests.get(url)
r.encoding = 'utf-8' 
data = r.json()
for i in range(20):
    print(data['articles'][i]['author'])



#用電ㄉ
'''
http://data.taipower.com.tw/opendata/apply/file/d007019/001.csv

http://210.69.35.216/od/data/api/88C78BC3-DF8F-4FC6-9E22-F65648B6CFD1?$format=csv

'''