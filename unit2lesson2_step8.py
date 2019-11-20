from selenium import webdriver
import time
import math
import os

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    last_name = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    submit = browser.find_element_by_tag_name("button")
    download = browser.find_element_by_id("file")

    first_name.send_keys("Irina")
    last_name.send_keys("Shmarkova")
    email.send_keys("irinashmarkova@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    download.send_keys(file_path)

    submit.click()

    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

