from selenium import webdriver
import time 
import unittest

# self.assertEqual('что должно быть', 'что есть', 'что произошло');
 
chrome = webdriver.Chrome()

class TestLogin(unittest.TestCase):
    def test_first_link(self):
        chrome.get("http://suninjuly.github.io/registration1.html")

        chrome.find_element_by_class_name("first").send_keys("Ivan")
        chrome.find_element_by_class_name("second").send_keys("Petrov")
        chrome.find_element_by_class_name("third").send_keys("email@mail.com")

        chrome.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = chrome.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual (welcome_text, "Congratulations! You have successfully registered!")
    
    def test_second_link(self):
        chrome.get("http://suninjuly.github.io/registration2.html")

        chrome.find_element_by_class_name("first").send_keys("Ivan")
        chrome.find_element_by_class_name("second").send_keys("Petrov")
        chrome.find_element_by_class_name("third").send_keys("email@mail.com")

        chrome.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = chrome.find_element_by_tag_name("h1")
        
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual (welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main() 
