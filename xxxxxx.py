'''import requests

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

print(response.text)

'''
'''
import json
import requests
import matplotlib.pyplot as plt

url = "https://www.dcard.tw/_api/forums/mood/posts?popular=false"

r = requests.get(url)
r.encoding = 'utf-8' 


data = json.loads(r.text)

gender = {"F":0, "M":0,"D":0}
for content in data:
    gender[content['gender']]+=1


kind = ['boy','girl']
data = [gender['M'],gender['F']]
plt.bar(kind ,data)
plt.yticks(range(0, 30, 2))
plt.show()
'''
'''
import matplotlib.pyplot as plt
import pandas as pd
url = 'http://opendataap2.hl.gov.tw/resource/files/2017-12-19/ae39065fdacd2100da6eb899aa8be0aa.csv'
sss = pd.read_csv(url)
#sss.encoding='big5'

bb=[]
for line in sss:
    bb.append(line)
    print(line)

sss.drop(sss.index[[12]],inplace=True)

plt.bar(sss['月份'] ,sss['太魯閣'])

plt.show()


# TODO: magic!
# TODO: another magic!

'''

'''
import requests
import pandas
import matplotlib.pyplot as plt

res = requests.get('https://graphs2.coinmarketcap.com/currencies/bitcoin/')
d = res.json()
print(d)
df = pandas.DataFrame(d)
print(df)

print(df['price_usd'])

df = df['price_usd']
date=[]
price=[]
for i in df:
	i[0] = pandas.to_datetime(i[0],unit='ms')
	date.append(i[0])
	price.append(i[1])

plt.plot(date,price)
plt.show()

'''


from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import json
import pandas
from datetime import datetime


kw_list = ['Blockchain']
pytrend = TrendReq(hl='en-US', tz=360)
pytrend.build_payload(kw_list , cat=0, timeframe='2015-01-01 2018-08-01', geo='TW', gprop='')
pytrend.interest_over_time().get('Blockchain')
preload = json.loads(pytrend.interest_over_time().to_json(orient='table'))['data']

df = pandas.DataFrame(preload)
print (df)

'''
print(df.iloc[4,0])
plt.bar(df.iloc[4,1] ,df.iloc[4,0])
plt.bar(df['date'] ,df['Airbnb'])
plt.plot(df['date'] ,df['Airbnb'])
plt.show()
'''

x = len(df)

c = []
for i in range(x):
    
    c.append(((df['date'][i])[2:7]))

p = pandas.DataFrame(c,columns=['a'])

print (p)
print(df['Blockchain'])

dd = pandas.concat([p,df['Blockchain']],axis=1)
print(dd)

plt.figure(figsize=(15,5))
plt.bar(dd['a'],dd['Blockchain'])

plt.xticks(rotation=90)#设置时间标签显示格式


plt.show()
