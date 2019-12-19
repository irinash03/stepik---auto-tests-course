from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_bin_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    bin_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")))
    assert bin_button.text == "Добавить в корзину"
