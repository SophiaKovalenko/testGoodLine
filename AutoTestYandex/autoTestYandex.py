'''
Для запуска программы требуется установить Python 3.5 или выше
Установить Selenium: pip install selenium
Скачать и скопировать в папку к Chrome драйвер https://chromedriver.chromium.org/downloads
'''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def goToSite(driver,site):
    driver.get(site)

def browser(path):
    driver = webdriver.Chrome(path)
    return driver

def findElementIdAndSendKeys(driver, name_elem, send_text):
    elem = driver.find_element_by_id(name_elem)
    elem.clear()
    elem.send_keys(send_text)
    return elem

if __name__ == '__main__':
    path_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe" #Заменить путь до драйвера
    driver = browser(path_driver)
    goToSite(driver, 'https://rasp.yandex.ru/')

    findElementIdAndSendKeys(driver, "from", "Кемерово")
    findElementIdAndSendKeys(driver, "to", "Москва")
    findElementIdAndSendKeys(driver, "when", "7 июля 2018").submit()

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "SegmentHeader")))
    except TimeoutError:
        print("A TimeoutError!")
    else:
        toggle = driver.find_elements_by_class_name("SearchTransfer__toggle")
        for t in range(len(toggle)):
            toggle[t].click()

        name = driver.find_elements_by_class_name('SegmentTitle__header')
        time = driver.find_elements_by_class_name('SearchSegment__duration')

        for i in range(len(name)):
            ico = None
            ico = name[i].find_element_by_class_name('Icon.Icon_flexShrinkZero.TransportIcon__icon')
            if ico:
                print(f"Рейс №{i + 1}: {name[i].text}; Продолжительность пути: {time[i].text}; Иконка есть!")
            else:
                print(f"Рейс №{i + 1}: {name[i].text}; Продолжительность пути: {time[i].text}; Иконки нет!")

        print(f"Всего рейсов на странице:{len(name)} из 5ти")
    finally:
        driver.quit()
        print("THE END")
