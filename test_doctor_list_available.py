import time
from test_login import test_login_to_mr_web_app as login
from selenium import webdriver


def test_doctor_list_mr_web_app():
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
    time.sleep(10)
    # login done ++++++++++=

    driver.find_element_by_xpath(
        '/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/ion-list[1]/ion-menu-toggle[2]/ion-item/ion-label').click()
    time.sleep(10)
    doctorNames = []
    for i in range(1, 4):
        doctorName_xpath = f'//*[@id="main-content"]/ng-component/ion-tabs/div/ion-router-outlet/app-connect/ion-content/ion-list/ion-item[{i}]/a/ion-label[1]'
        doctorName = driver.find_element_by_xpath(doctorName_xpath).text
        doctorNames.append(doctorName)
    print('lllllllllllllllll#####', len(doctorNames),doctorNames)
    lenthDoctorsName = len(doctorNames)
    assert lenthDoctorsName > 1
    driver.quit()
