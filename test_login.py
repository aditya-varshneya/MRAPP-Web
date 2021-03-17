import time
from selenium import webdriver
import app_config

# from selenium.common.exceptions import NoSuchElementException

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']


def test_login_to_mr_web_app():
    try:
        global driver
        driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
        driver.implicitly_wait(30)
        test_url = app_config.web_app_confg['web_url']
        driver.get(test_url)
        driver.maximize_window()

        usr_name = driver.find_element_by_xpath(
            '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-list/ion-item[1]/div/ion-input/input')
        usr_name.send_keys(web_usr)
        psw_box = driver.find_element_by_xpath(
            '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-list/ion-item[2]/ion-input/input')
        psw_box.send_keys(web_pass)
        # psw_box.send_keys('Abbo@123')

        driver.find_element_by_xpath(
            '//*[@id="main-content"]/page-login/ion-content/form[1]/ion-row/ion-col[1]/ion-button').click()
        time.sleep(10)
        # login done ++++++++++=
        dashboard_ele = driver.find_element_by_xpath('//*[@id="tab-button-home"]/ion-label').text
        assert dashboard_ele == "Dashboard", 'Login is not Successfully'
        print('output::', dashboard_ele)

        # driver.quit()
    except:
        raise Exception


def test_logout_mr_web_app():
    try:
        # clicking logout lable
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[7]/ion-item/ion-label').click()
        time.sleep(5)
        forget_password = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/page-login/ion-content/form[1]/ion-row/ion-col[2]').text
        assert forget_password == 'FORGOT PASSWORD?', 'Forgot Password? element not found '
        print('qqqqqqqq', forget_password)
        driver.quit()
    except:
        raise Exception
    finally:
        driver.quit()
