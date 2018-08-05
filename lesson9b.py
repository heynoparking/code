from requests_html import HTMLSession
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

session = HTMLSession()
url = 'https://shopee.tw/search/?keyword=%E6%A9%9F%E8%BB%8A'
response = session.get(url)

response.html.render() # 加上這一行即可，第一次跑他會花幾分鐘的時間下載 Chromium，用來跑 Javascript
elements = response.html.find('.shopee-item-card__text-name')
print(elements)