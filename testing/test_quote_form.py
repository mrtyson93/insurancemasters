from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .config import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def nav_to_quote():
    service=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    driver.get(URL)
    driver.maximize_window()

    go_to_quote_button = driver.find_element(By.NAME, "btn_get_a_quote")
    go_to_quote_button.click()

    continue_button = driver.find_element(By.NAME, "btn-continue-to-quote")
    continue_button.click()

    return driver


def test_about_you_fields_present():
    driver = nav_to_quote()

    first_name_field = driver.find_element(By.NAME, "txt-field-first-name")
    last_name_field = driver.find_element(By.NAME, "txt-field-last-name")
    address_field = driver.find_element(By.NAME, "txt-field-address")


    assert first_name_field.is_displayed()  
    assert last_name_field.is_displayed()  
    assert address_field.is_displayed()  

def test_nav_to_about_business():
    driver = nav_to_quote()

    go_to_about_business = driver.find_element(By.NAME, "btn-continue-about-business")
    go_to_about_business.click()

    current_url = driver.current_url

    assert current_url.endswith('quoteaboutbusiness')

    
def test_business_age_dropwdown():
    driver = nav_to_quote()

    go_to_about_business = driver.find_element(By.NAME, "btn-continue-about-business")
    go_to_about_business.click()

    age_dropdown = driver.find_element(By.NAME, "select-business-age-dropdown")
    age_dropdown.click()

    one_to_five = driver.find_element(By.NAME, "Age-Option-1-5 Years")
    assert one_to_five.is_displayed()  

def test_projected_revenue_dropdwon():
    driver = nav_to_quote()

    go_to_about_business = driver.find_element(By.NAME, "btn-continue-about-business")
    go_to_about_business.click()

    revenue_dropdown = driver.find_element(By.NAME, "select-projected-rev-dropdown")
    revenue_dropdown.click()

    one_to_five_million = driver.find_element(By.NAME, "$1M-$5M")
    assert one_to_five_million.is_displayed()  

def test_nav_to_results():
    driver = nav_to_quote()

    go_to_about_business = driver.find_element(By.NAME, "btn-continue-about-business")
    go_to_about_business.click()

    go_to_results = driver.find_element(By.NAME, "btn-submit-quote-details")
    go_to_results.click()

    current_url = driver.current_url

    assert current_url.endswith('result')