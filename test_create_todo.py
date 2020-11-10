import time
from selenium import webdriver
import app_config

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']


def test_create_todo_drname_mr_web_app():
    global driver
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

        # click on to_do tab of web app
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/ion-tab-bar/ion-tab-button[3]/ion-label').click()
        time.sleep(5)
        # clicking add button
        driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-to-do/ion-content/ion-fab').click()
        # clicking doctors dropdown
        driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/ion-item[1]/ionic-selectable/div/button').click()
        # search for A DOCTOR
        search_drname = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/ionic-selectable-modal/ion-header/ion-toolbar[2]/ion-searchbar/div/input')
        search_drname.send_keys('rakesh')
        time.sleep(5)

        # selecting search output of dr name
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-modal[2]/div/ionic-selectable-modal/ion-content/ion-list/ion-item-group/ion-item/ion-label').click()
        time.sleep(5)
        # getting dr name from search result
        original_drname = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/ion-item[1]/ionic-selectable/div/div[1]/span/div').text
        time.sleep(10)
        # clicking product list dropdown
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/ion-item[2]/ion-select').click()
        time.sleep(5)
        # clicking checkbox of product
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[3]/button/div/div[1]').click()
        time.sleep(3)
        # clicking ok button to submit
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-alert/div/div[4]/button[2]/span').click()
        time.sleep(3)
        # getting product name which is seelcted
        original_productname = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/ion-item[2]/ion-select//div[1]').text

        # enter details of product
        detail_box = driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/ion-item[3]/ion-input/input')
        detail_box.send_keys("Details of product goes here")
        time.sleep(5)
        # getting original time as == 08:21 PM
        global original_time
        original_time = driver.find_element_by_xpath(
            '//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-content/'
            'ion-row/ion-col[2]/ion-item/ion-datetime').text
        time.sleep(5)
        # clicking save btn
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-add-todo/ion-header/ion-toolbar/ion-buttons[2]/ion-button').click()
        # clicking pending btn
        driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-to-do/ion-header/ion-segment/ion-segment-button[2]').click()
        time.sleep(5)
        # getting final pending todos created values
        # dr name selected
        final_drname_ele = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-to-do/ion-content/div/div/ion-list/ion-item/ion-label/ion-label[1]')
        final_drname = final_drname_ele.text

        # text value of details entered
        final_detail_ele = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-to-do/ion-content/div/div/ion-list/ion-item/ion-label/ion-label[2]/small')
        final_detail = final_drname_ele.text
        # final time of created todos as ==  08:original_time,10 PM
        global final_time_ele
        final_time_ele = driver.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/ng-component/ion-tabs/div/ion-router-outlet/app-to-do/ion-content/div/div/ion-list/ion-item/ion-label/ion-label[3]/ion-button[2]').text
        print('111111111111111111111', original_drname, final_drname)
        assert original_drname.lower() == final_drname.lower(), 'Todo Dr names did not match'
    except:
        raise Exception
    finally:
        driver.quit()


try:
    def test_pending_todo_list_time_match():
        print('222222222222222222222', original_time, final_time_ele)
        assert original_time == final_time_ele, 'Created pending todo time did not match'
except NameError:
    raise NameError
