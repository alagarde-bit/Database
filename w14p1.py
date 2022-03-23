
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:51:47 2020

@author: alexl
"""
import configparser
import json
import pymysql

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

selectQuery = 'SELECT musicinfo\
               FROM theGrowlers;'

cursor.execute(selectQuery)

rows = cursor.fetchall()
for row in rows:
    musicInfo = row[0]
    jsondata = json.loads(musicInfo)
    trackID = jsondata['trackId']
    trackName = jsondata['trackName']
    collectionName = jsondata['collectionName']
    artistName = jsondata['artistName']
    trackPrice = jsondata['trackPrice']
    previewUrl = jsondata['previewUrl']
    trackTime = jsondata['trackTimeMillis']
    updateQuery = 'UPDATE theGrowlers\
                   SET trackID = %s,\
                       trackName = %s,\
                       collectionName = %s,\
                       artistName = %s,\
                       trackPrice = %s,\
                       previewUrl = %s,\
                       trackTimeMillis = %s\
                   WHERE musicinfo = %s;'
    cursor.execute(updateQuery, (trackID,
                                 trackName, 
                                 collectionName, 
                                 artistName,
                                 trackPrice, 
                                 previewUrl, 
                                 trackTime, 
                                 musicInfo))
    print(trackID,
          trackName,
          collectionName,
          artistName, 
          trackPrice, 
          previewUrl, 
          trackTime)
    print('')

