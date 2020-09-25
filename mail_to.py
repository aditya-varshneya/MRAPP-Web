import os
import pdfkit
import smtplib
from email.message import EmailMessage
import app_config

EMAIL_ADDRESS = app_config.email_config["EMAIL_USER"]
EMAIL_PASSWORD = app_config.email_config["EMAIL_PASS"]
contacts = app_config.email_config["contacts"]
# mrAppVersion = app_config.appium_config["app_cred"]["AppVersion"]
# mrAppVersion = app_config.appium_config["app_cred"]["AppVersion"]

msg = EmailMessage()
msg['Subject'] = f'MR Web App Automation Testing Report'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('''Hello,
Attached file is of Automation testing report For MR App.

Thanks
''')

html_files = os.listdir("Reports\HTML")

html_files = [os.path.join("Reports\HTML", file) for file in html_files]
print(html_files)
pdfkit.from_file(html_files,"Reports\\PDF\\MR_APP_Automation_Testing_Report.pdf")

with open('Reports\\PDF\\MR_APP_Automation_Testing_Report.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name.split('\\')[2]
#
msg.add_attachment(file_data, maintype='application', subtype='octate-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
