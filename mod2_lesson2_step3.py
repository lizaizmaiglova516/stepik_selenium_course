from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

#Найти х,y
x = browser.find_element_by_id("num1")
x_num = x.text
y = browser.find_element_by_id("num2")
y_num = y.text

#Посчитать сумму заданных чисел
result = str (int (x_num) + int (y_num))

#Выбрать в выпадающем списке значение равное расчитанной сумме

select = Select(browser.find_element_by_css_selector("select"))
select.select_by_value(result)

#Нажать кнопку "Submit"

button = browser.find_element_by_css_selector("button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()