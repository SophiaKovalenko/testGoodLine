from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://rasp.yandex.ru/')

from_elem = driver.find_element_by_id("from")
from_elem.clear()
from_elem.send_keys("Кемерово")

to_elem = driver.find_element_by_id("to")
to_elem.clear()
to_elem.send_keys("Москва")

when_elem = driver.find_element_by_id("when")
when_elem.clear()
when_elem.send_keys("7 июля 2018")
when_elem.submit()
print('beforeSleep')
time.sleep(5)

q_len = len(driver.find_elements_by_class_name('SearchTransfer__toggle'))  # выпадающий список маршрута


title_raise = driver.find_elements_by_class_name('SegmentTitle__title')
print("Кол-во рейсов: ", len(title_raise)-q_len) #Рейсев всего 3 штуки

time_elem = driver.find_elements_by_class_name('SearchSegment__duration')
print("Время в пути: ",time_elem) #Рейсев всего 3 штуки

icon_elem = driver.find_elements_by_class_name('TransportIcon__icon')
print("Кол-во иконок транспорта: ",len(icon_elem)) #Рейсев всего 3 штуки

test_title = driver.find_elements_by_class_name('SegmentTitle')
print(test_title)
for i in range(len(test_title)):
    sub_Title_element = None
    sub_Title_element = test_title[i].find_elements_by_tag_name('figure')
    if sub_Title_element: print("YES:",sub_Title_element)

#button_search = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div[1]/div/div[5]/form/button[2]')
#button_search.send_keys(Keys.RETURN)