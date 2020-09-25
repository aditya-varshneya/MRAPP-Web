cd C:\Users\AMIT\PycharmProjects\MRwebApp
pytest -v --html=Reports/HTML/1.login_test_report.html --self-contained-html  test_login.py &

cd C:\Users\AMIT\PycharmProjects\MRwebApp
pytest -v --html=Reports/HTML/2.DrList_test_report.html --self-contained-html  test_doctor_list_available.py &

cd C:\Users\AMIT\PycharmProjects\MRwebApp
pytest -v --html=Reports/HTML/3.ProdList_test_report.html --self-contained-html  test_create_todo.py &

cd C:\Users\AMIT\PycharmProjects\MRwebApp
python -m mail_to
