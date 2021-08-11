from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

browser.find_element_by_id("book").click()

#assert "successful" in message.text
x = browser.find_element_by_id("input_value").text
def calc(x):
    return str(math.log (abs(12*math.sin(int(x)))))
result = calc(x)
input = browser.find_element_by_id('answer')
input.send_keys(result)

button = browser.find_element_by_id("solve")
button.click()