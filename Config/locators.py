from selenium.webdriver.common.by import By


class Locators:
    epicButton = (By.XPATH,"//label[contains(text(),'Epic Link:')]")
    epicText = (By.XPATH, "//a[@class='aui-label ghx-label-2']")
    titleText = (By.XPATH, "//h1[@id='summary-val']")
    typeButton = (By.XPATH,"//label[contains(text(),'Type:')]")
    typeText = (By.XPATH,"//span[@id='type-val']")
    affectedVersionButton = (By.XPATH,"//label[contains(text(),'Affects Version/s:')]")
    affectedVersionText = (By.XPATH,"//span[@id='versions-val']")
    fixVersionButton = (By.XPATH, "//strong[@title='Fix Version/s']")
    fixVersionText = (By.XPATH, "//span[@id='fixfor-val']")
    storyPointButton=(By.XPATH,"//strong[@title='Story Points']")
    storyPointText=(By.XPATH,"//div[@id='customfield_10002-val']")
    acceptanceCriteriaButton=(By.XPATH,"//strong[@title='Acceptance Criteria']")
    acceptanceCriteriaText=(By.XPATH,"//div[@id='field-customfield_10300']")
    descriptionButton=(By.XPATH,"//h4[contains(text(),'Description')]")
    descriptionText=(By.XPATH,"//div[@id='description-val']")
    #descriptionText//div[@id='descriptionmodule']//child::div[@class='mod-content']
    componentButton_optional = (By.XPATH, "//label[contains(text(),'Component/s:')]")
    componentText_optional = (By.XPATH, "span[@id='components-val']")
    labelsButton_optional = (By.XPATH, "//label[contains(text(),'Labels:')]")
    labelsText_optional = (By.XPATH, "//div[@class='labels-wrap value']")
    priorityButton=(By.XPATH,"//label[contains(text(),'Priority:')]")
    priorityText=(By.XPATH,"//span[@id='priority-val']")
    complianceButton=(By.XPATH,"//strong[@title='Compliance Type']")
    approvalButton=(By.XPATH,"//label[contains(text(),'Approval Category:')]")
    approvalText=(By.XPATH,"//div[@class='field-group']")
    assigneeText=(By.XPATH,"//span[@id='assignee-val']")
    reporterText=(By.XPATH,"//span[@id='reporter-val']")
    sprintButton=(By.XPATH,"//strong[@title='Sprint']")
    sprintText=(By.XPATH,"//div[@id='customfield_10004-val']")






    #(By.XPATH,"")


