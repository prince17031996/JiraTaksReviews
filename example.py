import time

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.basePage import Basepage

driver = webdriver.Chrome()
driver.get("https://jira.jnj.com/browse/JCVZ-1030")
#https://jira.jnj.com/browse/JCVZ-1030
#driver.maximize_window()
driver.implicitly_wait(10)

#element=driver.find_element(By.XPATH,"//div[@class='ReactVirtualized__Grid__innerScrollContainer']//child::div[@data-index]")
count=0


for x in range(0, 200):

    try:
        action = driver.find_element(By.XPATH,f"//div[@data-index='{x}']"
                                         f"//div[@class='step-container sc-CtfFt fiKMAr']"
                                         f"//div[@class='step-content sc-laTMn ijLfRy']"
                                         f"//div[contains(@class,'step-fields sc-hGoxap')]"
                                         f"//div[@class='text-field-holder field-holder sc-itybZL jtGvFH sc-fjmCvl lmUaVJ']"
                                         f"//div[@class='text-field-container sc-iRbamj bhOdCd']//div[@tabindex='-1']"
                                         f"//div[@data-testid='Action-view']//div[@class='test-step-field-content']")

        time.sleep(1)
        if action:
            print("this is action text",action.text)
        # Scroll down by dynamically increasing pixels using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();",action)

        time.sleep(1)
        # Add a small delay to allow content to load
    except (NoSuchElementException, TimeoutException) as e:
        print("Error: come out")
        break

print("Scrolling to the beginning of the webpage...")
time.sleep(1)
scrollTo= driver.find_element(By.XPATH,"//h4[contains(text(),'Test Details')]")
driver.execute_script("arguments[0].scrollIntoView();", scrollTo)
#print("Scrolled to the beginning.")
for x in range(0, 200):
    try:

        expected = driver.find_element(By.XPATH, f"//div[@data-index='{x}']//div[@class='step-container sc-CtfFt fiKMAr']//div[@class='step-content sc-laTMn ijLfRy']//div[contains(@class, 'step-fields sc-hGoxap')]//div[@class='text-field-holder field-holder sc-itybZL jtGvFH sc-fjmCvl lmUaVJ']//div[@class='text-field-container sc-iRbamj bhOdCd']//div[@tabindex='-1']//div[@data-testid='Expected Result-view']")


        time.sleep(1)
        if expected:
            print("this is expected result",expected.text)
        # Scroll down by dynamically increasing pixels using JavaScript

        driver.execute_script("arguments[0].scrollIntoView();", expected)
        time.sleep(1)
        # Add a small delay to allow content to load
    except (NoSuchElementException, TimeoutException) as e:
        print("Error: come out")
        break




#print(count)
time.sleep(5)












