
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

def Num1():

    while True:
            r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.202624.014)"}
            p = {'edata' :'Hello'}
            st =post('http://codespace.ir' , data=p,headers=r)
            if st.status_code == 200 :
                logging.warn("Ok Server1 ")
            else:
                logging.warn("Error Net  1 :((")
            time.sleep(225)


    

Thread(target=Num1).start()

