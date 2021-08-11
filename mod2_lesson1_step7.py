from selenium import webdriver
import time 
import math

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)

#Найти на ней элемент-картинку, который является изображением сундука с сокровищами
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
x = browser.find_element_by_xpath('//h2/img[@src="images/chest.png"]').get_attribute('valuex')

#Посчитать математическую функцию от x (сама функция остаётся неизменной)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

#Ввести ответ в текстовое поле
input = browser.find_element_by_id('answer').send_keys(y)

#Отметить checkbox "I'm the robot"
checkbox = browser.find_element_by_id('robotCheckbox').click()

#Выбрать radiobutton "Robots rule!"
radiobutton = browser.find_element_by_id('robotsRule').click()

#Нажать на кнопку "Submit"
button = browser.find_element_by_css_selector("button.btn")
button.click()
