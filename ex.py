from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jira.jnj.com/browse/AADF-27928")
driver.maximize_window()

title_locator = (By.XPATH, "//123h1[@id='summary-val']")
type_locator = (By.XPATH, "//123label[contains(text(),'Type:')]")
epic_locator = (By.XPATH, "//strong[@title='Epic Link']")

def visible(by_locator):
    try:
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        print("this is elements",len(elements))
        if elements:
            print("Element is visible on the webpage")
            return True
    except:
        print("Element is not visible")
        return False

print(visible(epic_locator))
print(visible(type_locator))
