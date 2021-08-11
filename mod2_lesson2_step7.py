from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

#Считать значение для переменной x
button = browser.find_element_by_css_selector("button.btn")
button.click()

#Проскроллить страницу вниз
#Ввести ответ в текстовое поле
input = browser.find_element_by_id('answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(result)

#Выбрать checkbox "I'm the robot
checkbox = browser.find_element_by_id('robotCheckbox').click()

#Переключить radiobutton "Robots rule!"
radiobutton = browser.find_element_by_id('robotsRule').click()

#Нажать на кнопку "Submit"
button = browser.find_element_by_css_selector("button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()