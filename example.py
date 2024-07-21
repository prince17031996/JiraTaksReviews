import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome()
executionKey="AFJX-11576"
testIssueKey="AFJX-11010"
driver.get(f"https://jira.jnj.com/secure/XrayExecuteTest!default.jspa?testExecIssueKey={executionKey}&testIssueKey={testIssueKey}")
driver.maximize_window()
time.sleep(2)
scrollTo=driver.find_element(By.XPATH,"//div[@class='execution-steps-module-heading mod-header']")
driver.execute_script("arguments[0].scrollIntoView();", scrollTo)
time.sleep(2)
try:
    # Example of finding a button using XPath with correct usage
    button = driver.find_element(By.XPATH, "(//button[@class='aui-button raven-has-results'])[1]")
    button.click()


    print("Button clicked successfully")
except NoSuchElementException as e:
    print("errpr")
time.sleep(5)
# Loop through potential actual result elements
for x in range(1, 100):
    time.sleep(2)
    try:
        # Construct XPath for each actual result element
        button = driver.find_element(By.XPATH,f"(//button[@class='aui-button raven-has-results'])[{x}]")
        time.sleep(5)

        button.click()
        actualResult = driver.find_element(By.XPATH,f"(//div[@class='raven-field-wiki-view']//div[@class='field-content text-wrap'])[{x}]//p")
        driver.execute_script("arguments[0].scrollIntoView();", actualResult)
        print(f"actual result {x} is:", actualResult.text)
        #click on button

        # Wait for the element to be visible



        # Scroll element into view (optional)


        # Print the text content of the element
       # if actualResult:
        #    print(f"actual result {x} is:", actualResult.text)

    except (NoSuchElementException,TimeoutException):
        print(f"Timeout waiting for actualResult {x} to be visible")
        break


# Close the browser window
driver.quit()
