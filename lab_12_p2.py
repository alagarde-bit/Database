# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:24:28 2020

@author: alexl
"""

import pymysql
import configparser
import random


config = configparser.ConfigParser()
config.read_file(open('credentials.txt'))
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']
dbschema = 'alagarde' 


dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()

username = input('What is your username?')
email = username + "@bigbank.com"
print(username)
print(email)

PINlength = 4
PINdigit = 0
PIN = ''
while PINdigit < PINlength:
    randomNum = random.randint(0, 9)
    PIN = PIN + str(randomNum)
    PINdigit += 1


userNum = None
insertQuery = 'INSERT INTO userDatabase (userID, userName, email, PIN)\
                VALUES (%s, %s, %s, %s)'
                
cursor.execute(insertQuery, (userNum, username, email, PIN))
print('Row added!')

dbconn.close()
