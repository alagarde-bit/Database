# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:55:42 2020

@author: alexl
"""

import pymysql
import configparser

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
username = input("Enter your username: ")

usernameQuery = 'SELECT userID, PIN\
                 FROM userDatabase\
                 WHERE userName = %s'
cursor.execute(usernameQuery, (username))
result = cursor.fetchone()

print("The current PIN for that username is: " + result[1])

newPin = input("Enter your desired new PIN: ")

updateQuery = 'UPDATE alagarde.userDatabase\
                SET PIN = %s\
                WHERE userID =' + str(result[0])
cursor.execute(updateQuery, (newPin))

print("Thank you, your information has been updated.")
dbconn.close()
 #str(result[0]
