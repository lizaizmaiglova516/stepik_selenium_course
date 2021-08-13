from selenium import webdriver
import time 
import unittest

# self.assertEqual('что должно быть', 'что есть', 'что произошло');
 
class TestLogin(unittest.TestCase):
    def input(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration1.html")


        self.browser.find_element_by_class_name(("form-control.first").send_keys("Ivan"))
        self.browser.find_element_by_class_name(("form-control.second").send_keys("Petrov"))
        self.browser.find_element_by_class_name(("form-control.third").send_keys("email@mail.com"))

        self.browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        self.time.sleep(1)

    # находим элемент, содержащий текст
        self.welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = welcome_text_elt.text

        self.assertEqual (welcome_text, "Congratulations! You have successfully registered!")
    
if __name__ == "__main__":
    unittest.main() 