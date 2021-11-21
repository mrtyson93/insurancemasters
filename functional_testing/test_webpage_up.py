from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_webpage_up():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    title = "Insurance Masters"
    assert title == driver.title
 
def test_nav_to_your_business():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()

    state_dropdown = Select(driver.find_element(By.NAME, "select-state-dropdown"))
    state_dropdown.select_by_value('CA')
    
    get_quote_button = driver.find_element(By.NAME, "btn-get-quote")
    get_quote_button.click()

    about_your_business_header = driver.find_element(By.NAME, "header-about-your-business")
    assert about_your_business_header.is_displayed()  
