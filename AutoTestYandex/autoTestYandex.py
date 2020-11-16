'''
pip install selenium
pip install pytest
pip install requests
Скачать и скопировать в папку к Chrome драйвер https://chromedriver.chromium.org/downloads
'''

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

def goToSite(driver,site):
    driver.get(site)

def browser():
    print("-def browser():")
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    #yield driver
    #driver.quit()
    return driver

def findElementIdAndSendKeys(driver, name_elem, send_text):
    print("-def findElementIdAndSendKeys(driver, name_elem, send_text):")
    elem = driver.find_element_by_id(name_elem)
    elem.clear()
    elem.send_keys(send_text)
    return elem

if __name__ == '__main__':
    driver = browser()
    goToSite(driver, 'https://rasp.yandex.ru/')

    findElementIdAndSendKeys(driver, "from", "Кемерово")
    findElementIdAndSendKeys(driver, "to", "Москва")
    findElementIdAndSendKeys(driver, "when", "7 июля 2018").submit()
    
    time.sleep(5)
    #driver.implicitly_wait(10)
    #wait = WebDriverWait(driver, 10)
    #e = wait.until(EC.invisibility_of_element((By.CLASS_NAME,  'SegmentHeader')))
    #print(e)

    name = driver.find_elements_by_class_name('SegmentTitle__header')
    print("name", name)
    title = driver.find_elements_by_class_name('SegmentTitle__title')
    #print("title", title)
    number = driver.find_elements_by_class_name('SegmentTitle__number')
    #print("number", number)
    time = driver.find_elements_by_class_name('SearchSegment__duration')
    #print('time', time)
    for i in range(len(title)):
        sub_ico = None
        sub_ico = name[i].find_element_by_class_name('Icon.Icon_flexShrinkZero.TransportIcon__icon') #SegmentTitle__title
        if sub_ico:
            print(f"Рейс №{i+1}: {number[i].text} {title[i].text}; Продолжительность пути: {time[i].text}; Иконка есть!")
        else:
            print(f"Рейс №{i+1}: {number[i].text} {title[i].text}; Продолжительность пути: {time[i].text}; Иконки нет!")

    print(f"Всего рейсов на странице:{len(name)} из 5ти")
