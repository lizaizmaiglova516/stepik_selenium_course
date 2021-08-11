from selenium import webdriver
import os 
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

#Заполнить текстовые поля: имя, фамилия, email
input1 = browser.find_element_by_xpath("//div/input[@placeholder = 'Enter first name']")
input1.send_keys('Ivan')
input2 = browser.find_element_by_xpath("//div/input[@placeholder = 'Enter last name']")
input2.send_keys('Petrov')
input3 = browser.find_element_by_xpath("//div/input[@placeholder = 'Enter email']")
input3.send_keys('Petrov@mail.com')

#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "test.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

#Нажать кнопку "Submit"
button = browser.find_element_by_css_selector("button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()