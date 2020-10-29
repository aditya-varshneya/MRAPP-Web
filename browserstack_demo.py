# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium import webdriver
import app_config

# from selenium.common.exceptions import NoSuchElementException

web_usr = app_config.web_app_confg['login_usr']
web_pass = app_config.web_app_confg['login_pass']

desired_cap = {
    'os_version': 'Catalina',
    'resolution': '1920x1080',
    'browser': 'Safari',
    'browser_version': '13.1',
    'os': 'OS X',
    'name': 'BStack-[Python] Sample Test',  # test name
    'build': 'BStack Build Number 1',  # CI/CD job or build name
    'console':"errors"

}
driver = webdriver.Remote(
    command_executor='https://rajeshpachar1:uo8LtDH4j43qn8nbi8uy@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)


# driver.get("http://base-mr-app.s3-website.ap-south-1.amazonaws.com/login")


def test_login_to_mr_web_app():
    try:
        global driver
        # driver = webdriver.Chrome("C:\\Users\\AMIT\\PycharmProjects\\MRwebApp\\chromedriverexe\\chromedriver.exe")
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
        assert forget_password == 'Forgot Password?', 'Forgot Password? element not found '
        print('qqqqqqqq', forget_password)
    except:
        raise Exception
    finally:
        driver.quit()
