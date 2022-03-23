# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:32:34 2020

@author: alexl
"""

import pymysql
import configparser
import csv

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

filename = 'peopleDOB.csv'
myRows = []
try:
    with open(filename, 'r') as myCSV:
        data = csv.reader(myCSV)
        next(myCSV)
        for row in data:
            myRows.append(row)
        myCSV.close()
except FileNotFoundError:
    print("No file!")
    
updateQuery = 'UPDATE peopleData\
                SET dob = %s\
                WHERE peopleID = %s'

for item in myRows:
    pID = item[0]
    dob = item[1]
    cursor.execute(updateQuery, (dob, pID))
    print(dob, pID)
    
dbconn.close()