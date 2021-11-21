from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .config import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_webpage_up():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    title = "Insurance Masters"
    assert title == driver.title
 
def test_nav_to_user_settings():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    go_to_quote_button = driver.find_element(By.NAME, "btn_get_a_quote")
    go_to_quote_button.click()

    state_dropdown = driver.find_element(By.NAME, "select-state-dropdown")
    assert state_dropdown.is_displayed()  

def test_valid_state_found():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    go_to_quote_button = driver.find_element(By.NAME, "btn_get_a_quote")
    go_to_quote_button.click()

    state_dropdown = driver.find_element(By.NAME, "select-state-dropdown")
    state_dropdown.click()

    texas_option = driver.find_element(By.NAME, "state-option-TX")
    assert texas_option.is_displayed()  

def test_invalid_state_not_found():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    go_to_quote_button = driver.find_element(By.NAME, "btn_get_a_quote")
    go_to_quote_button.click()

    state_dropdown = Select(driver.find_element(By.NAME, "select-state-dropdown"))
    state_options = state_dropdown.options
    state_options_states = [state_option.text for state_option in state_options]

    assert "Michigan" not in state_options_states


def test_nav_to_quote_after_continue():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    driver.get(URL)
    driver.maximize_window()
    
    go_to_quote_button = driver.find_element(By.NAME, "btn_get_a_quote")
    go_to_quote_button.click()

    state_dropdown = Select(driver.find_element(By.NAME, "select-state-dropdown"))
    state_dropdown.select_by_value('CA')

    continue_button = driver.find_element(By.NAME, "btn-continue-to-quote")
    continue_button.click()

    current_url = driver.current_url

    assert current_url.endswith('quoteaboutyou')

