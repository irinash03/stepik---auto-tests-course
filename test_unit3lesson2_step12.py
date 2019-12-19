from selenium import webdriver
import time
import unittest

class Test_registration1(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_class_name("first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_class_name("third")
        email.send_keys("ivan@test.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

class Test_registration2(unittest.TestCase):
        def test_registration2(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element_by_class_name("first")
            first_name.send_keys("Ivan")
            last_name = browser.find_element_by_css_selector("[placeholder='Input your last name']")
            last_name.send_keys("Petrov")
            email = browser.find_element_by_class_name("third")
            email.send_keys("ivan@test.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()


