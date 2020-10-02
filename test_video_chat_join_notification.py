import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import app_config

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']


def test_video_chat_sms_notification_entry_on_history_mr_web_app():
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

        # clicking video detailing tab
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[4]/ion-item/ion-label').click()
        time.sleep(10)

        # clicking Add button
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-video-detailing/ion-content/ion-fab/ion-fab-button').click()
        time.sleep(3)

        # clicking doctors dropdown
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-video-detailing/ion-content/ion-item[2]/ionic-selectable/div').click()
        time.sleep(3)

        # search for dr
        search_box = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/ionic-selectable-modal/ion-header/ion-toolbar[2]/ion-searchbar/div/input//div[2]/div[1]')
        search_box.send_keys('vikas')
        time.sleep(5)

        # selecting from the search result
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/ionic-selectable-modal/ion-content/ion-list/ion-item-group/ion-item/ion-icon').click()

        # clicking the ok button to confirm
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/ionic-selectable-modal/ion-footer/ion-toolbar/ion-row/ion-col[2]/ion-button').click()
        time.sleep(5)

        # clicking superwiser toggle button
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-video-detailing/ion-content/ion-item[3]/ion-toggle').click()

        # clicking superviser checkbox
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-video-detailing/ion-content/div/ion-item[2]/ion-checkbox').click()

        # clickinfg the product list dropdown
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-video-detailing/ion-content/ion-item[4]/ion-select').click()

        # clicking the product pop up list
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[3]/button[1]/div/div[1]').click()

        # clicking the product list ok button
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[4]/button[2]').click()
        time.sleep(3)

        # clicking the create video room button
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-video-detailing/ion-content/ion-button').click()
        time.sleep(5)

        # clicking the okay button
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[3]/button').click()
        time.sleep(5)
        # clicking send button
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-video-detailing/ion-content/ion-row/ion-col[3]/ion-button').click()
        time.sleep(5)

        # clicking okay button
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[3]/button').click()
        time.sleep(10)

        # getting time stamp text on video room created as == '2020-09-30 12:22 AM'
        datetime_video_room = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-video-detailing/ion-content/div/div/ion-list/ion-card[1]/div/ion-card-header/ion-item/a/ion-label[2]/small').text
        date_stamp = datetime_video_room.split(' ')[0]
        global time_stamp
        time_stamp = datetime_video_room[-8:]
        # clicking connect tab
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/ion-tab-bar/ion-tab-button[2]').click()
        time.sleep(5)

        # clicking dr name
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-connect/ion-content/ion-list/ion-item[1]').click()

        # clicking view history
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-doctor-profile/ion-content/ion-row[2]/ion-col/ion-button').click()
        time.sleep(5)

        # getting sms entry text
        global sms_entry_text
        sms_entry_text = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-view-history/ion-content/ion-list/ion-item[1]/ion-label/ion-label[2]/span').text

        assert date_stamp in sms_entry_text, 'Date stamp is not present in sms notification'
        driver.quit()
    except:
        raise Exception
    finally:
        driver.quit()


try:
    def test_time_stamp_in_notificatio():
        assert time_stamp in sms_entry_text, 'Time stamp not presnt in the sms notificatio'
except NameError:
    raise NameError
