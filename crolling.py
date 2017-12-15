
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import datetime

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('http://203.244.128.145')

driver.switch_to_frame("Main")


my_id = ''
my_pw = ''

driver.find_element_by_class_name('input_id').send_keys(my_id)

driver.find_element_by_name('password').send_keys(my_pw, Keys.RETURN)


#로그인 후 



#time = datetime.datetime.now().strftime('%H:%M:%S')
'''
수강번호
1. 인공지능 3738
2. 대중매체와문화 1058
3. 영화와문화 4538
4. 창업과기업가정신 2332
'''


lecture = [ 3738, 2332, 4538, 1058 ]

for i in lecture:
    driver.get('http://203.244.128.145/servlets/stud/sugang?attribute=sugang_save&sugang_no='+str(i)+'&fake=Fri Aug 18 2017 '+datetime.datetime.now().strftime('%H:%M:%S')+' GMT+0900 (대한민국 표준시)')
    print(str(i)+" 시도")

    try:
        Alert(driver).accept()
        print('실패!')
    except:
        print('성공!')
    driver.back()
    driver.implicitly_wait(0.1)



    

'''

#첫번째과목
driver.get('http://203.244.128.145/servlets/stud/sugang?attribute=sugang_save&sugang_no=3727&fake=Thu Aug 17 2017 '+datetime.datetime.now().strftime('%H:%M:%S')+' GMT+0900 (대한민국 표준시)')

Alert(driver).accept()

driver.back()
driver.implicitly_wait(0.1)
#두번째 과목

driver.get('http://203.244.128.145/servlets/stud/sugang?attribute=sugang_save&sugang_no=3727&fake=Thu Aug 17 2017 '+datetime.datetime.now().strftime('%H:%M:%S')+' GMT+0900 (대한민국 표준시)')

Alert(driver).accept()
driver.back()
'''

