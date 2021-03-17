import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import app_config

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']


def test_sms_sent_to_doctor_mr_web_app():
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
        # login done ++++++++++=
        # clicking connect tab
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[2]/ion-item/ion-label').click()
        time.sleep(5)
        # clicking 2nd dr name lable
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-connect/ion-content/ion-list/ion-item[2]/a').click()
        time.sleep(5)
        # clicking email icon of dr profile
        driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-card/ion-row/ion-col[5]').click()
        time.sleep(2)
        # clicking the 2nd email product for email template
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-product-list/ion-content/div/div/ion-list/ion-item[3]/ion-label/ion-label').click()

        driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-product-list/ion-content/div/div/ion-list').click()
        time.sleep(2)
        # clicking the template of the product
        # getting email header text
        global email_header_text_prev
        email_header_text_prev = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-templates/ion-content/div/div/ion-list/ion-item/ion-label/ion-label').text
        driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-templates/ion-content/div/div/ion-list/ion-item').click()
        time.sleep(5)

        # time.sleep(5)
        # # clicking the send butoon to send thw sms
        # submit_button = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-edit-template/ion-content/ion-row/ion-col[5]/ion-button')
        # # scrolling down
        # # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # driver.execute_script("arguments[0].scrollIntoView();",submit_button)
        # clicking the submitting button
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-edit-template/ion-content/ion-row/ion-col[2]/ion-button').click()
        time.sleep(5)
        # clicking the okay button to confirm sending the sms
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[3]/button/span').click()
        # again clicking the dr name to view history
        # clicking 2nd dr name lable
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-connect/ion-content/ion-list/ion-item[2]/a').click()
        time.sleep(5)
        # clicking view history button
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[2]/ion-col/ion-button').click()
        time.sleep(5)
        # get templatename
        sent_email_name = driver.find_element_by_xpath('//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-view-history/ion-content/ion-list/ion-item[1]/ion-label/ion-label[2]/span').text
        # getting first ement properties for assert
        # first date time as == '02:27 PM, 28 Sep 2020'
        first_entry_date_time = driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-view-history/ion-content/ion-list/ion-item[1]/ion-label/ion-label[1]').text
        second_entry_date_time = driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-view-history/ion-content/ion-list/ion-item[2]/ion-label/ion-label[1]').text
        global mail_title_text
        mail_title_text = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-view-history/ion-content/ion-list/ion-item[1]/ion-label/ion-label[2]/span').text
        assert first_entry_date_time != second_entry_date_time, 'Time of two entry is same'
        print('Date time entry campaire::', first_entry_date_time, second_entry_date_time)
        assert sent_email_name == 'Automation Template'
    except:
        raise Exception
    finally:
        driver.quit()


# try:
#     def test_email_name_check():
#         print('Test mail name entry campaire::', email_header_text_prev, mail_title_text)
#         assert email_header_text_prev == mail_title_text, 'Test mail name did not match'
# except NameError:
#     raise NameError
