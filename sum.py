from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

from handler.chatgpt_selenium_automation import ChatGPTAutomation

f_clear = open("./summary.txt", "w", encoding="utf-8")
f_clear.close()
chrome_driver_path = r"C:/Users/civbf/source/repos/top-news-summary/chromedriver.exe" 
chrome_path = r'"C:/Program Files/Google/Chrome/Application/chrome.exe"'

chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

p = ""
prompt= "이 뉴스를 3개에서 5가지 불렛 포인트로 요약해줘. 아주 중요한 거야:"

with open("result.txt", "r",  encoding="utf-8") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        if index%2==1:
            second_prompt = lines[index:index+2]
            p = prompt+second_prompt[0]+second_prompt[1]
            p=p.replace("\'", "").replace("\t","").replace("\"","").replace("[", "").replace("]", "").replace("...", "").replace("\n", "")

            chatgpt.send_prompt_to_chatgpt(str(p))
            response = chatgpt.return_last_response()
    chatgpt.save_conversation("./summary.txt")
    
    file.close()


chatgpt.quit()