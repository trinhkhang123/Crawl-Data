from selenium import webdriver

import os

from dotenv import load_dotenv

import re

import pandas as pd

import openpyxl

from time import sleep 

from bs4 import BeautifulSoup

from lxml import etree

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

load_dotenv()

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

style =  {
    "responce":"background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/JvsiB3mMXWu.png&quot;); background-position: 0px -193px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;",
    "time": "background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/eu2LG4UKGHk.png&quot;); background-position: 0px -138px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;",
    "ticket" : "background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/y_/r/CkMEofY62Oj.png&quot;); background-position: 0px -495px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;",
    "ognaizer" : "background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/t7aaabCFzOl.png&quot;); background-position: 0px -235px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;",
    "who" : "background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/JvsiB3mMXWu.png&quot;); background-position: 0px -214px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;",
    "location" : "background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/WxIcblanueJ.png&quot;); background-position: 0px -1006px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;",
}
ID = {
    "responce": 1,
    "time":2,
    "ticket" : 3,
    "ognaizer" : 4,
    "who" : 5,
    "location" : 6
    }


browser = webdriver.Chrome( chrome_options=option,service=Service(ChromeDriverManager().install()))

user_name = os.getenv('user_name')

pass_word = os.getenv('pass_word')

browser.get("http://facebook.com")

# browser.maximize_window()

send_user_name  = browser.find_element(By.ID,"email").send_keys(user_name)

send_pass_word  = browser.find_element(By.ID,"pass").send_keys(pass_word)

login_user = browser.find_element(By.NAME,"login").click()

page_limit = 1

page_count = 0

sleep(10)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a/div[1]/div[2]').click()

browser.implicitly_wait(30)
# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/span/span
# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[5]/label/div/div/div/div/div[1]/div/div[1]/div/div/div/div/span

# browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div').click()

# browser.implicitly_wait(2)

# browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[5]/label/div/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()


