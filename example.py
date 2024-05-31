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
driver.maximize_window()
driver.implicitly_wait(10)

#element=driver.find_element(By.XPATH,"//div[@class='ReactVirtualized__Grid__innerScrollContainer']//child::div[@data-index]")
count=0
"""element=driver.find_element(By.XPATH,(f"//div[@data-index='{count}']"))
if element:
    print("True")
else:
    print("False")"""

""""action=driver.find_element(By.XPATH,"//div[@data-testid='Action-view']//child::div[@class='test-step-field-content']")
expectedResult=driver.find_element(By.XPATH,"//div[@data-testid='Expected Result-view']//child::div[@class='test-step-field-content'][]")
for x in range(10):
    try:
        if driver.find_element(By.XPATH,(f"//div[@data-index='{x}']")):
            print(count)
            if driver.find_elements(By.XPATH,(f"(//div[@data-testid='Action-view']//child::div[@class='test-step-field-content'])[{x+1}]")):
                #l.append(driver.find_elements(By.XPATH,(f"(//div[@data-testid='Action-view']//child::div[@class='test-step-field-content'])[{x+1}]")).text)
            count+=1
    except NoSuchElementException:
        break"""""

""""l=list()
pixel=180
data=driver.find_elements(By.XPATH,"(//div[@data-testid='Action-view']//child::div[@class='test-step-field-content'])")
print(len(data))
for x in range(1,len(data)+1):
    try:
        z=driver.find_element(By.XPATH,(f"(//div[@data-testid='Action-view']//child::div[@class='test-step-field-content'])[{x}]"))
        if z:
            print(z.text)
        driver.execute_script(f"window.scrollBy(0, {pixel});")
        pixel += 180

    except NoSuchElementException:
        break"""""
#l = list()
#data = driver.find_elements(By.XPATH,"(//div[@data-testid='Action-view']//child::div[@class='test-step-field-content'])")
#print(len(data))

scroll_amount = 180
pixel=0
#  test data insdex //div[@id='test-step-index-10']
# //div[@data-index='9']
#parent //div[@data-index='9']//div[@class='step-container sc-CtfFt fiKMAr']//div[@class='step-content sc-laTMn ijLfRy']//div[@class='step-fields sc-hGoxap bDhqzx']
#//div[@data-index='9']//div[@class='step-container sc-CtfFt fiKMAr']//div[@class='step-content sc-laTMn ijLfRy']//div[@class='step-fields sc-hGoxap bDhqzx']//div[@class='text-field-holder field-holder sc-itybZL jtGvFH sc-fjmCvl lmUaVJ']//div[@class='text-field-container sc-iRbamj bhOdCd']//div[@id='field_NATIVE_STEP_NATIVE_33732_7480306']//div[@data-testid='Action-view']//div[@class='test-step-field-content']
for x in range(0, 20):
    try:
        z = driver.find_element(By.XPATH,f"//div[@data-index='{x}']//div[@class='step-container sc-CtfFt fiKMAr']//div[@class='step-content sc-laTMn ijLfRy']//div[@class='step-fields sc-hGoxap bDhqzx']//div[@class='text-field-holder field-holder sc-itybZL jtGvFH sc-fjmCvl lmUaVJ']//div[@class='text-field-container sc-iRbamj bhOdCd']//div[@tabindex='-1']//div[@data-testid='Action-view']//div[@class='test-step-field-content']")
        time.sleep(1)
        if z:
            print(z.text)
        # Scroll down by dynamically increasing pixels using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();",z)

        time.sleep(1)
        # Add a small delay to allow content to load
    except (NoSuchElementException, TimeoutException) as e:
        print("Error: come out")
        break



#print(count)
time.sleep(5)












