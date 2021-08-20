import numbers
from selenium import webdriver
import time 
import math
import pytest
import unittest

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

    class TestPage():

        message = ""
        numbers = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

        @pytest.mark.parametrize('pages','link')
        def test_correct_message(self, browser, numbers):
            
            link = f"https://stepik.org/lesson/{numbers}/step/1"
            browser.get(link)
            browser.implicity_wait(10)
            browser.find_element_by_css_selector('.textarea').send_keys(str(math.log(int(time.time()))))
            browser.implicity_wait(10)
         
            self.button = browser.find_element_by_css_selector(".submit-submission").click()
            browser.implicity_wait(10)
            message = browser.find_element_by_xpath("//[@class='smart-hints__hint']").text 
            assert "Correct!" != message
            self.pages = message
            print(self.pages)

        assert message == False

        if __name__ == "__main__":
            unittest.main()