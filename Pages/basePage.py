import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def doClick(self, bylocator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(bylocator)).click()
        except TimeoutException:
            print("Element is not visible on the webpage.")
            return None


    def isVisible(self,bylocator):
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(bylocator))
            if elements:
               # print("Element is visible on the webpage")
                return True
        except(NoSuchElementException, TimeoutException):
            #print("Element is not visible")
            return False


    def getText(self, bylocator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(bylocator))
            #print("Text is visible ")
            if element:
                return element.text
        except TimeoutException:
            #print("text is not visible on the webpage.")
            return False
    def getTextTestSteps(self, bylocator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(bylocator))
            #print("Text is visible ")
            if len(element.text)>5:
                return True
        except (NoSuchElementException, TimeoutException) as e:
            #print("text is not visible on the webpage.")
            return False

    def getTitle(self, bylocator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(bylocator))
           # print("title is visible ")
            return self.driver.title
        except TimeoutException:
            print("title is not visible on the webpage.")
            return False

    def scroll(self,bylocator):
        self.driver.execute_script("arguments[0].scrollIntoView();", bylocator)


