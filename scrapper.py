import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict

def scrapHolders(page = 0):
    #the page index on the explorer is odd it uses the last on each page to reference the next list so there is no easy way to get multiple pages
    #unless we loop through all of the pages
    URL = "https://explorer.fuse.io/accounts"
    driver = webdriver.Chrome()

    driver.get(URL)
    page = driver.find_element_by_tag_name('body')
    for i in range(5):
        page.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.quit()

    token_list = soup.find_all('div', attrs={'class', 'tile'})

    holders = OrderedDict()

    for holder in token_list:
        balance = float(holder.find('span', attrs={'class', 'tile-title'}).text[:-5].replace(',',''))
        address = holder.find("a")['href'].split('/')[-1]
        holders[address] = balance

    return holders