
import random
import time
import logging
import sys
import requests
import time
from requests import post
import datetime
from termcolor import colored
import os
from os import system, name
import logging
from threading import Thread
import httpx
import time
from threading import Thread
import redis
import logging

Fruit1 = "018b8d548a10d487f4dd2be5a7dc094b" 
Fruit2 = "4063c15405c1dac5a621610840b274f8"

def Num1():

    r = redis.StrictRedis(
    host="redis-18829.c305.ap-south-1-1.ec2.cloud.redislabs.com", port=18829, decode_responses=True,
    username="hossein",
    password="Hosseinhm123@")
    b = "ASDFGHJKL:{POIUYTREW"
    a = r.hget("SMS", b)

    while a == None:
        print(colored(" ! Your License is not valid ! " , 'red'))
        exit()
        b = "ASDFGHJKL:{POIUYTRE"     
        a = r.hget("SMS", b)

        if (a != None):
            pass

    if a == "Expired":
        print('\n')
        print(colored("Your Account Expired ! "  ,'red'))
        exit()
    while True:
            r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit1}"}
            p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
            st =post('http://iran.fruitcraft.ir/cards/collectgold' , data=p,headers=r)
            if st.status_code == 200 :
                logging.warn("Ok Server1 ")
            else:
                logging.warn("Error Net  1 :((")
            time.sleep(225)



def Num2():

    r = redis.StrictRedis(
    host="redis-18829.c305.ap-south-1-1.ec2.cloud.redislabs.com", port=18829, decode_responses=True,
    username="hossein",
    password="Hosseinhm123@")
    b = "ASDFGHJKL:{POIUYTREW"
    a = r.hget("SMS", b)

    while a == None:
        print(colored(" ! Your License is not valid ! " , 'red'))
        exit()
        b = "ASDFGHJKL:{POIUYTRE"     
        a = r.hget("SMS", b)

        if (a != None):
            pass

    if a == "Expired":
        print('\n')
        print(colored("Your Account Expired ! "  ,'red'))
        exit()
    while True:
            r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit1}"}
            p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
            st =post('http://iran.fruitcraft.ir/cards/collectgold' , data=p,headers=r)
            if st.status_code == 200 :
                logging.warn("Ok Server2 ")
            else:
                logging.warn("Error Net  2 :((")
            time.sleep(225)
            


            

    

Thread(target=Num1).start()
Thread(target=Num2).start()

