from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import json
import pandas

kw_list = ['Airbnb']
pytrend = TrendReq(hl='en-US', tz=360)
pytrend.build_payload(kw_list , cat=0, timeframe='2015-01-01 2018-08-01', geo='TW', gprop='')
pytrend.interest_over_time().get('Airbnb')
preload = json.loads(pytrend.interest_over_time().to_json(orient='table'))['data']
df = pandas.DataFrame(preload)

x = len(df)
c = []
for i in range(x):
    c.append(((df['date'][i])[2:7]))
p = pandas.DataFrame(c,columns=['a'])

dd = pandas.concat([p,df['Airbnb']],axis=1)
print(dd)

plt.figure(figsize=(0,8))
plt.bar(dd['a'],dd['Airbnb'], width = 0.7,facecolor='lightslategray')
plt.xticks(rotation=90)
plt.legend(loc="upper left")
plt.xlabel(u'性别')
plt.ylabel(u'人数')
plt.show()
