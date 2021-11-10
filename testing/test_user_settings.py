from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .config import URL
from selenium.webdriver.common.by import By

def test_webpage_up():
    print(f'test webpage is up')
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    title = "Insurance Masters"
    assert title == driver.title
 
def test_nav_to_user_settings():
    print(f'test nav to user settings')
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    go_to_quote_button = driver.find_element(By.NAME, "btn_get_a_quote")
    go_to_quote_button.click()

    state_dropdown = driver.find_element(By.NAME, "select-state-dropdown")
    assert state_dropdown.is_displayed()  