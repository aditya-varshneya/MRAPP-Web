import os
from webdriver_manager.chrome import ChromeDriverManager
web_app_confg = {
    "web_url":"http://base-mr-app.s3-website.ap-south-1.amazonaws.com/login",
    "login_usr":"9643357782",
    # "login_pass":"Cipl@123"
    "login_pass":"Thbm@123",
    "chromedriverexe_path":ChromeDriverManager().install()
}


email_config = {
    "EMAIL_USER": "adityakumar@thb.co.in",
    "EMAIL_PASS": "aditya061287",
    #"contacts": ['amitkumar@thb.co.in'],
    "contacts": ["nitin@thb.co.in", "rajesh@thb.co.in", "adityakumar@thb.co.in", "vikassingh@thb.co.in",
"rakesh@thb.co.in", 'amitkumar@thb.co.in', "satyendra@thb.co.in"]

}
