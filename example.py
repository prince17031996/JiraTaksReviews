from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jira.jnj.com/browse/JCVZ-998")
driver.maximize_window()

approvalText=(By.XPATH, "//div[@class='field-group']")
#print(approvalText.text)
def getText(bylocator):
    try:
        element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(bylocator))
        # print("Text is visible ")
        if element:
            return (element.text)

    except NoSuchElementException:
        # print("text is not visible on the webpage.")
        return False

if getText(approvalText)=="NONE":
    print("failed")
else:
    print("passed")


