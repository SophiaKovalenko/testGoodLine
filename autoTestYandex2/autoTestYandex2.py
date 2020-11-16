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

    button_list = driver.find_elements_by_class_name('RadioButton__buttonLable')
    for button in button_list:
        if button.text == 'Автобус':
            button_bus = button
    button_bus.click()

    findElementIdAndSendKeys(driver, "from", "Кемерово проспект Ленина")
    findElementIdAndSendKeys(driver, "to", "Кемерово Бакинский переулок")
    findElementIdAndSendKeys(driver, "when", "среда").submit()

    error_elem = None

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "PopupError")))
    except TimeoutError:
        print("A TimeoutError!")
    else:
        error_elem = driver.find_elements_by_class_name('PopupError')
        for err in error_elem:
            if err.text == 'Пункт отправления не найден':
                print("Тест пройден:", err.text)
                break
    finally:
        driver.quit()
        print("THE END")
