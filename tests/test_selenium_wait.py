
#pytest -v --driver Chrome --driver-path C:\Users\Администратоp\Desktop\SkillFactory\Module_25\chromedriver.exe test_selenium_wait.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('http://petfriends1.herokuapp.com/login')


@pytest.fixture(autouse=True)
def log_in():
    driver.find_element_by_id('email').send_keys('6ij4l5rg9l@esiix.com')
    driver.find_element_by_id('pass').send_keys('123')
    driver.find_element_by_css_selector('button[type="submit"]').click()
    assert driver.find_element_by_tag_name('h1').text == 'PetFriends'

    yield

    driver.quit()


def test_explicitly_wait_pet_grid():
    # driver.get('http://petfriends1.herokuapp.com/all_pets')
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.task3.fill'))
    )
    assert element

def test_implicitly_wait_pet_profiles():
    driver.implicitly_wait(10)
    # driver.get('http://petfriends1.herokuapp.com/all_pets')
    assert driver.find_element_by_class_name('card-img-top')
    assert driver.find_element_by_class_name('card-title')
    assert driver.find_element_by_class_name('card-text')