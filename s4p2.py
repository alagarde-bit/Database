# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:56:00 2020

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

joinQuery = 'SELECT bbUserDatabase.userName, bbWordList.word\
             FROM bbUserDatabase\
             INNER JOIN bbWordList\
                 ON bbWordList.hashOfWord = bbUserDatabase.hashedPassword\
             ORDER BY bbUserDatabase.userID'

cursor.execute(joinQuery)

users = cursor.fetchall()
for item in users:
    user = item[0]
    password = item[1]
    print('The password for', user, 'is', password + '.')

dbconn.close()