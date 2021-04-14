import time
from selenium import webdriver
import app_config

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']
chromeexe_path = app_config.web_app_confg['chromedriverexe_path']


def test_doctor_list_mr_web_app():
    global driver
    try:
        driver = webdriver.Chrome(chromeexe_path)
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

        # clicking connect tab
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[2]/ion-item/ion-label').click()
        time.sleep(10)
        doctorNames = []
        for i in range(1, 4):
            doctorName_xpath = f'//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-connect/ion-content/ion-list/ion-item[{i}]/a/ion-label[1]'
            doctorName = driver.find_element_by_xpath(doctorName_xpath).text
            doctorNames.append(doctorName)
        print('lllllllllllllllll#####', len(doctorNames), doctorNames)
        lenthDoctorsName = len(doctorNames)
        assert lenthDoctorsName > 1

    except:
        raise Exception
    finally:
        driver.quit()
