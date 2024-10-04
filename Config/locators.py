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
    descriptionText=(By.XPATH,"//div[@id='description-val']//child::div[@class='user-content-block']")
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
    dueDateButton=(By.XPATH,"//label[@for='duedate']")
    dueDateText=(By.XPATH,"//span[@id='due-date']")

    #TestScript Locators
    issueResolutionButton=(By.XPATH,"//strong[@title='Issue Resolution']")
    issueResolutionText=(By.XPATH,"//div[@id='customfield_10200-val']")
    testCategoryButton = (By.XPATH,"//strong[@title='Test Category']")
    testCategoryText = (By.XPATH,"//div[@id='customfield_13801-val']")
    #actualResultText=(By.XPATH,f"//div[@data-index='{x}']//div[@class='step-container sc-CtfFt fiKMAr']//div[@class='step-content sc-laTMn ijLfRy']//div[contains(@class,'step-fields sc-hGoxap')]//div[@class='text-field-holder field-holder sc-itybZL jtGvFH sc-fjmCvl lmUaVJ']//div[@class='text-field-container sc-iRbamj bhOdCd']//div[@tabindex='-1']//div[@data-testid='Action-view']//div[@class='test-step-field-content']")
    expectedResultText=(By.XPATH)
    testTypeButton=(By.XPATH,"//ul[@id='test-details']//child::strong[text()='Type:']")
    testTypeText=(By.XPATH,"//strong[@title='Test type']")
    issueLinkButton=(By.XPATH,"//h4[@id='linkingmodule-label']")
    testExecutionButton=(By.XPATH,"//td//a[@class='issue-link']")

    #bug Locators
    rootCauseButton=(By.XPATH,"//label[contains(text(),'Root Cause:')]")
    severityButton=(By.XPATH,"//label[contains(text(),'Severity:')]")

    #Test Execution Locators
    actualResultCount=(By.XPATH,"//div[@id='actions-module2']//div[@tabindex='0']//button[@class='aui-button raven-has-results']")
    actualResultText=(By.XPATH,"")




    #(By.XPATH,"")


