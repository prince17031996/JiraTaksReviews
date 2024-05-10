from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jira.jnj.com/browse/JCVZ-998")
driver.maximize_window()

#title_locator = (By.XPATH, "//h1[@id='summary-val']")
#type_locator = (By.XPATH, "//label[contains(text(),'Type:')]")
#epic_locator = (By.XPATH, "//strong[@title='Epic Link']")
#epic=driver.find_elements(By.XPATH, "123//strong[@title='Epic Link']")
approvalText=driver.find_elements(By.XPATH,"//div[@class='field-group']")

def visible1(epic):
    if len(epic) > 0:
        print("Element is visible on the webpage")
        return True
    else:
        print("Element is not visible")
        return False
#print(visible1(epic))


def visible(by_locator):
    elements = driver.find_elements(*by_locator)
    if len(elements) > 0:
        print("Element is visible on the webpage")
        return True
    else:
        print("Element is not visible")
        return False

#print(visible(epic_locator))
#print(visible(type_locator))
