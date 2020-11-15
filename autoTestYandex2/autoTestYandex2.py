from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://rasp.yandex.ru/')

from_elem = driver.find_element_by_id("from")
from_elem.clear()
from_elem.send_keys("Кемерово проспект Ленина")

to_elem = driver.find_element_by_id("to")
to_elem.clear()
to_elem.send_keys("Кемерово Бакинский переулок")

when_elem = driver.find_element_by_id("when")
when_elem.clear()
when_elem.send_keys("среда")

button_list = driver.find_elements_by_class_name('RadioButton__buttonLable')

for button in button_list:
    if button.text == 'Автобус':
        button_bus = button
button_bus.click()

when_elem.submit()
time.sleep(5)

error_elem = None
error_elem = driver.find_elements_by_class_name('PopupError')
for err in error_elem:
    if err.text == 'Пункт отправления не найден':
        print("YES:",err.text)
        break
