from selenium import webdriver
import time
import math
import os

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")

    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    input = browser.find_element_by_id("answer")
    submit = browser.find_element_by_css_selector("[type = 'submit']")

    x = x_element.text
    y = calc(x)
    input.send_keys(y)
    submit.click()

    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

