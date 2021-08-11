from selenium import webdriver
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

#Нажать на кнопку
submit = browser.find_element_by_css_selector('[type = "submit"]').click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

#На новой странице решить капчу для роботов, чтобы получить число с ответом
x = browser.find_element_by_id("input_value").text
def calc(x):
    return str(math.log (abs(12*math.sin(int(x)))))
result = calc(x)
input = browser.find_element_by_id('answer')
input.send_keys(result)

button = browser.find_element_by_css_selector("button.btn")
button.click()