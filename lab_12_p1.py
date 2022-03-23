# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:07:47 2020

@author: alexl
"""
import pymysql
import configparser

config = configparser.ConfigParser()
config.read_file(open('credentials.txt'))
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']

dbschema = 'movielens' 
dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()

print('###########################')
print('Great Movie Viewer Bot 9000')
print('###########################')

chooseGenre = input('What genre are you interested in? ')

print("Top 10 Highest ranked" + " " + chooseGenre + " movies: ")

query ='SELECT movies.title, COUNT(ratings.rating)\
        FROM movies\
        INNER JOIN ratings\
            ON ratings.movie_id = movies.movie_id\
        INNER JOIN movie_genres\
            ON movie_genres.movie_id = movies.movie_id\
        INNER JOIN genres\
            ON genres.genre_id = movie_genres.genre_id\
        WHERE ratings.rating = 5 AND genres.genre = %s\
        GROUP BY 1\
        ORDER BY 2 DESC\
        LIMIT 10'
        
cursor.execute(query, (chooseGenre))
result = cursor.fetchall()
counter = 1
for row in result:
    print(counter, '. ', row[0], ' ,(', row[1], ' "5" ratings)', sep= '')
    counter+= 1
    
print("")
print("Thanks for playing with the Movie Viewer Bot 9000.")
    
    

dbconn.close()