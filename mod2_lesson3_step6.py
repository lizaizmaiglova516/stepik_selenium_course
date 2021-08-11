from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

#Нажать на кнопку
button = browser.find_element_by_css_selector("button.btn")
button.click()

#Переключиться на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

#Решить капчу
x = browser.find_element_by_id("input_value").text
def calc(x):
    return str(math.log (abs(12*math.sin(int(x)))))
result = calc(x)
input = browser.find_element_by_id('answer')
input.send_keys(result)

button = browser.find_element_by_css_selector("button.btn")
button.click()

