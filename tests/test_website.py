from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebsite:
    def test_website_open(self):
        with webdriver.Chrome("/home/sweb/chromedriver/chromedriver") as driver:
            driver.get("https://ya.ru")
            elem = driver.find_element(By.ID, "text")
            assert elem, "Поле поиска не найдено"
            driver.quit()
