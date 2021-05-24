import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    pytest.driver = webdriver.Chrome('C:/temp/chromedriver.exe')
    pytest.driver.implicitly_wait(10)

    yield pytest.driver

    pytest.driver.quit()