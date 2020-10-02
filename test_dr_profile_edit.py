import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import app_config

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']


def test_sms_sent_to_doctor_mr_web_app():
    try:
        driver = webdriver.Chrome("C:\\Users\\AMIT\\PycharmProjects\\MRwebApp\\chromedriverexe\\chromedriver.exe")
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
        # login done ++++++++++=
        # clicking connect tab
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[2]/ion-item/ion-label').click()
        time.sleep(5)
        # clicking 2nd dr name lable
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-connect/ion-content/ion-list/ion-item[2]/a').click()
        time.sleep(5)
        # getting dr info from profile page
        dr_name_start = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[1]/ion-label').text
        global dr_specialization_start
        dr_specialization_start = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[2]/ion-chip[1]/ion-label').text
        global dr_mobile_start
        dr_mobile_start = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[2]/ion-chip[3]/ion-label').text
        global dr_email_start
        dr_email_start = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[2]/ion-chip[4]/ion-label').text

        # clicking EDIT button of dr profile
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-header/ion-toolbar/ion-buttons[2]/ion-button').click()
        time.sleep(2)
        # editing dr name
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[1]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys('Vaibhav Dixitt')
        # editting dr specialization
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[2]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys('General Practionerr')
        # editting dr email
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[3]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys('vaibhavv@thb.co.in')
        # editting dr mobile no
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[4]/ion-row/ion-col[2]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys('9205461341')
        # submitting for update
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-button').click()
        time.sleep(5)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++====================+++++++++++++++++++
        # editting to its original value of dr profile
        # clicking EDIT button of dr profile
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-header/ion-toolbar/ion-buttons[2]/ion-button').click()
        time.sleep(2)
        # editing dr name
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[1]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys(dr_name_start)
        # editting dr specialization
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[2]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys(dr_specialization_start)
        # editting dr email
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[3]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys(dr_email_start)
        # editting dr mobile no
        profile_name_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-item[4]/ion-row/ion-col[2]/ion-input/input')
        profile_name_box.clear()
        time.sleep(2)
        profile_name_box.send_keys(dr_mobile_start)
        # submitting for update
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/app-edit-doctor/ion-content/ion-button').click()
        time.sleep(5)
        # getting dr profile after update
        dr_name_updated = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[1]/ion-label').text
        global dr_specialization_updated
        dr_specialization_updated = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[2]/ion-chip[1]/ion-label').text
        global dr_mobile_updated
        dr_mobile_updated = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[2]/ion-chip[3]/ion-label').text
        global dr_email_updated
        dr_email_updated = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[1]/ion-col[2]/ion-chip[4]/ion-label').text

        assert dr_name_start == dr_name_updated, 'Dr profile name not updated'
        driver.quit()
    except:
        raise Exception
    finally:
        driver.quit()


try:
    def test_dr_specialization_check():
        assert dr_specialization_start == dr_specialization_updated, 'Test Dr specialization did not match '


    def test_dr_email_check():
        assert dr_email_start == dr_email_updated, 'Test Dr profile email did not match '


    def test_dr_mobile_check():
        assert dr_mobile_start == dr_mobile_updated, 'Test Dr profile mobile did not match '
except NameError:
    raise NameError
