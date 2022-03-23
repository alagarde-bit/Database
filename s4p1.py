# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:26:11 2020

@author: alexl
"""

import pymysql
import configparser
import hashlib

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

selectQuery = 'SELECT word\
               FROM bbWordList;'
             
updateQuery = 'UPDATE bbWordList\
               SET hashOfWord = %s\
               WHERE word = %s;'
               
cursor.execute(selectQuery)

words = cursor.fetchall()
for item in words:
    word = item[0]
    hashWord = hashlib.md5(word.encode()).hexdigest()
    cursor.execute(updateQuery, (hashWord, word))
    print('The Hash of', word, 'is', hashWord + '.', 'Table updated!')
    
dbconn.close()