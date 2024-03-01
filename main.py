from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re


driver = webdriver.Chrome()
driver.get( "https://trends.google.com/trends/trendingsearches/daily?geo=KR"
)
time.sleep(1)

soup = BeautifulSoup((driver.page_source.encode('utf-8')), 'html.parser')
news_titles = soup.find_all('div', class_='summary-text')
f_clear = open("./result.txt", "w", encoding="utf-8")
f_clear.close()
f = open("./result.txt", "a", encoding="utf-8")

for idx, title in enumerate(news_titles):
    if idx>=7:
        break
    news_title = str(title.get_text())
    news_link = title.find('a')['href']

    try:
        driver.get(news_link)
    except:
        pass
    time.sleep(2)

    news_soup = BeautifulSoup(driver.page_source, 'html.parser')
    news_content = news_soup.find_all("p")

    if news_content:
        f.write(str(news_title))
        if len(news_content)>0:
            for news in news_content:
                trimmed =re.sub(r"[^ㄱ-ㅣ0-9 가-힣\s]", "", str(news)).replace("\n", "")
                f.write(str(trimmed))
    else:
        print("no news content")
f.close()

driver.quit()
