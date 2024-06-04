from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
# 使用 Safari 的 WebDriver
driver = webdriver.Safari()
# 開啟 Fast.com 網路測速網頁
driver.get('https://fast.com')
# 取得網頁原始碼
html = driver.page_source
# 指定 lxml 作為 parser 取得 HTML
soup = bs(html,'lxml')
# 等待測速
while( not len(soup.select('div.speed-results-container.succeeded')) > 0): # 若尚未出現.succeesed
    html = driver.page_source
    soup = bs(html,'lxml')
# 取得網速
speed = soup.select_one('div.speed-results-container.succeeded')
unit = soup.select_one('div.speed-units-container.succeeded')
# 顯示網速
print(speed.get_text() + ' ' + unit.get_text())
# 等待1秒
sleep(1)
# 關閉瀏覽器
driver.quit()