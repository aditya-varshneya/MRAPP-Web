import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import pdfkit
import time
from PyPDF2 import PdfFileMerger



if os.path.exists("Automation_Report.pdf"):
  os.remove("Automation_Report.pdf")
else:
  print("The file does not exist")

time.sleep(2)
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_file("1.login_logout_web_app_test_report.html", "1.login_logout_web_app_test_report.pdf", configuration=config)
pdfkit.from_file("2.Doctor_list_available_web_app_test_report.html", "2.Doctor_list_available_web_app_test_report.pdf", configuration=config)
pdfkit.from_file("3.Create_todo_web_app_test_report.html", "3.Create_todo_web_app_test_report.pdf", configuration=config)
pdfkit.from_file("4.Product_list_web_app_test_report.html", "4.Product_list_web_app_test_report.pdf", configuration=config)
pdfkit.from_file("5.SMS_Sent_web_app_test_report.html", "5.SMS_Sent_web_app_test_report.pdf", configuration=config)
pdfkit.from_file("6.EMAIL_Sent_web_app_test_report.html", "6.EMAIL_Sent_web_app_test_report.pdf", configuration=config)
pdfkit.from_file("7.DR_Profile_Edit_web_app_test_report.html", "7.DR_Profile_Edit_web_app_test_report.pdf", configuration=config)

time.sleep(5)

source_dir = os.getcwd()
merger = PdfFileMerger()
for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items,import_bookmarks=False)

merger.write('Automation_Report.pdf')
merger.close()

email_user = 'adityakumar@thb.co.in'
email_send = "satyendra@thb.co.in,nitin@thb.co.in,rajesh@thb.co.in," \
             "rakesh@thb.co.in,amitkumar@thb.co.in,vikassingh@thb.co.in"
email_copy = 'adityakumar@thb.co.in'
password = base64.b64decode("YWRpdHlhMDYxMjg3").decode("utf-8")


#outlook = win32.Dispatch('outlook.application')


message = MIMEMultipart()
message['From'] = email_user
message['To'] = email_send
message['Cc'] = email_copy
message['Subject'] = "Automation Testing Report - Web MR Application"
body = "Hi All, Please find attached Automation report"
message.attach(MIMEText(body, 'plain'))
# attachment
filename = "Automation_Report.pdf"

files = [filename]
dir_path = "C:/Automation/MRAPP-Web/Reports/HTML"
for f in files:
    file_path = os.path.join(dir_path, f)
    attachment = open(file_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment;filename= %s' % f)
    message.attach(part)

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(email_user, password)
text = message.as_string()
server.sendmail(message["From"], message["To"].split(",") + message["Cc"].split(","), text)
server.quit()
print("Mail Sent")