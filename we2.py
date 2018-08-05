from bs4 import BeautifulSoup
from selenium import webdriver

try:
    url = 'https://www.zeczec.com/categories?type=one-time'
    driver = webdriver.Chrome()  # '選擇使用 Chrome 來開啟網頁'
    driver.get(url)
    content = driver.page_source 
finally:
    print('ok')
#     driver.close()
    driver.quit()


soup = BeautifulSoup(content, 'html.parser')
tag = soup.find(class_='f7').text
print(tag)