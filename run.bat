cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/1.login_logout_web_app_test_report.html --self-contained-html "test_login.py" &

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/2.Doctor_list_available_web_app_test_report.html --self-contained-html  "test_doctor_list_available.py" &

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/3.Create_todo_web_app_test_report.html --self-contained-html  "test_create_todo.py" &

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/4.Product_list_web_app_test_report.html --self-contained-html  "test_product_list_available.py" &

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/5.SMS_Sent_web_app_test_report.html --self-contained-html  "test_sms_sending.py" &

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/6.EMAIL_Sent_web_app_test_report.html --self-contained-html  "test_email_sending.py" &

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web
pytest -v --tb=no --html=Reports/HTML/7.DR_Profile_Edit_web_app_test_report.html --self-contained-html  "test_dr_profile_edit.py"&

cd C:\Users\Lenovo\Documents\GitHub\MRAPP-Web\Reports\HTML
python "mail_to.py"
