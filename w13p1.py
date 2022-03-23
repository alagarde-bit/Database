# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:36:39 2020

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

import csv
filename = 'peopleData.csv'
myRows = []
try:
    with open(filename, 'r') as myCSV:
        data = csv.reader(myCSV)
        next(myCSV)
        for row in data:
            myRows.append(row) 
        myCSV.close()
except FileNotFoundError:
    print('No file!')

insertQuery  = 'INSERT INTO peopleData\
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
userID = None
for item in myRows:
    fn = item[0]
    ln = item[1]
    co = item[2]
    ad = item[3]
    city = item[4]
    county = item[5]
    state = item[6]
    zipCode = item[7]
    phone1 = item[8]
    phone2 = item[9]
    email = item[10]
    web = item[11]
    cursor.execute(insertQuery,(userID,fn,ln,co,ad,city,county,state,zipCode,phone1,phone2,email,web))

dbconn.close()