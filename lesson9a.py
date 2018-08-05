import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

sss = json.loads(response.text)


with open ('music_show.json','r+', encoding='utf-8') as f:

    json.dump(sss, f)

with open ('music_show.txt','w+') as p :

    for i in range(len(sss)) :

    
        a = sss[i]['title'] + ":" + sss[i]['startDate'] + "~" + sss[i]['endDate'] + "\n"
        p.write(a)
    
    

    