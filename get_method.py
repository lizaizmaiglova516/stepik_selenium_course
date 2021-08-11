from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
with webdriver.Chrome() as browser:
    # открываем браузер, передаем в него ссылку link
    browser.get(link)
    form1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    form1.send_keys("Keys")
    # в первое поле для регистрации отпраляется значение keys, аналогично еще 4 раза для необязательных
    # полей тоже
    form2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    form2.send_keys("Keys")
    form3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
    form3.send_keys("Keys")
    form4 = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.first_class > input")
    form4.send_keys("Keys")
    form5 = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.second_class > input")
    form5.send_keys("Keys")
    # ищем кнопку, находим кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # нажимаем на кнопку
    button.click()
    time.sleep(5)
    # находим элемент welcome text по тегу (копипаст из задания)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    # проверяем, не падает ли тест
    assert welcome_text == "Congratulations! You have successfully registered!"
    time.sleep(10)




