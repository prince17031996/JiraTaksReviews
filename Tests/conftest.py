import pytest
from selenium import webdriver
@pytest.fixture(params=["chrome"],scope ='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    request.cls.driver = driver

    yield driver
    driver.quit()