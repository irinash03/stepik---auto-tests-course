from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1")
# Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
# Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("num1")
    a = a.text
    print(a)
    b = browser.find_element_by_id("num2")
    b = b.text
    sum1 = int(a) + int(b)


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum1))

    submit = browser.find_element_by_css_selector("[type = 'submit']")
    submit.click()

    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

