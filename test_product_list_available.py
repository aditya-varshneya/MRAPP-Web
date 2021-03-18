import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import app_config

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']


def test_product_list_mr_web_app():
    global driver
    try:
        driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
        driver.implicitly_wait(50)
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

        # click on to_do tab of web app
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/ion-tab-bar/ion-tab-button[3]/ion-label').click()
        time.sleep(5)
        # clicking add button
        driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-to-do/ion-content/ion-fab').click()
        time.sleep(5)
        # clicking product list dropdown
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/ion-item[2]/ion-select').click()
        time.sleep(15)
        products_list = []

        # for i in range(0, 1):
        #     # prod_xpath_ele = f'/html/body/app-root/ion-app/ion-alert/div/div[3]/button[{i}]'
        #     prod_xpath_ele = f'//*[@id="alert-input-27-0"]/div/div[2]'
        #     # clicking product list dropdown
        #     product_name = driver.find_element_by_xpath(prod_xpath_ele).text
        #     products_list.append(product_name)
        # print(products_list)

        # prod_xpath_ele = f'/html/body/app-root/ion-app/ion-alert/div/div[3]/button[{i}]'
        prod_xpath_ele = f'/html/body/app-root/ion-app/ion-alert/div/div[3]/button/div/div[2]'
        # clicking product list dropdown
        product_name = driver.find_element_by_xpath(prod_xpath_ele).text
        products_list.append(product_name)
        print(products_list)
        assert len(products_list) > 0, 'Product list are not present'
        assert products_list[0] == 'ASTHALIN'
    except NoSuchElementException:
        raise Exception
    finally:
        driver.quit()
