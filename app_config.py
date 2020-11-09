import os

web_app_confg = {
    "web_url":"http://base-mr-app.s3-website.ap-south-1.amazonaws.com/login",
    "login_usr":"9643357782",
    "login_pass":"Thbm@123"
}


email_config = {
    "EMAIL_USER": os.environ.get('EMAIL_USER'),
    "EMAIL_PASS": os.environ.get('EMAIL_PASS'),
    "contacts": ['amitkumar@thb.co.in'],
    # "contacts": ["nitin@thb.co.in", "rajesh@thb.co.in", "adityakumar@thb.co.in", "vikassingh@thb.co.in",
    #              "rakesh@thb.co.in", "vaibhav@thb.co.in", 'amitkumar@thb.co.in', "satyendra@thb.co.in"]

}
