from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#Считать значение для переменной x
x_element = browser.find_element_by_xpath('//label/span[@id="input_value"]')
x = x_element.text
y = calc(x)

#Ввести ответ в текстовое поле
input = browser.find_element_by_class_name('form-control')
input.send_keys(y)

#Отметить checkbox "I'm the robot"
checkbox = browser.find_element_by_xpath("//div/input[@type='checkbox']").click()

#Выбрать radiobutton "Robots rule!"
radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

#Нажать на кнопку Submit
button = browser.find_element_by_css_selector("button.btn")
button.click()