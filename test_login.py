import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 1}
# chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome("\\chromedriverexe\\chromedriver.exe", chrome_options=chrome_options)
# test_url = f'https://abbottmrapp.hlthclub.in/login'
# driver.get(test_url)
# driver.maximize_window()

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 1}
# chrome_options.add_experimental_option("prefs", prefs)


def test_login_to_mr_web_app():
    global driver
    driver = webdriver.Chrome("C:\\Users\\AMIT\\PycharmProjects\\MRwebApp\\chromedriverexe\\chromedriver.exe")
    driver.implicitly_wait(50)
    test_url = 'https://abbottmrapp.hlthclub.in'
    driver.get(test_url)
    driver.maximize_window()

    usr_name = driver.find_element_by_xpath(
        '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-list/ion-item[1]/div/ion-input/input')
    usr_name.send_keys('9643357782')
    psw_box = driver.find_element_by_xpath(
        '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-list/ion-item[2]/ion-input/input')
    psw_box.send_keys('Abbo@123')

    driver.find_element_by_xpath(
        '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-row/ion-col[1]/ion-button').click()
    time.sleep(5)
    dashboard_ele = driver.find_element_by_xpath('//*[@id="tab-button-home"]/ion-label').text

    assert dashboard_ele == "Dashboard", 'Login is not Successfully'

    # driver.quit()


def test_logout_mr_web_app():
    # clicking logout lable
    driver.find_element_by_xpath(
        '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[6]/ion-item/ion-label').click()
    driver.find_element_by_xpath(
        '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-list/ion-item[1]/div/ion-input/input')
    time.sleep(10)
    driver.quit()
