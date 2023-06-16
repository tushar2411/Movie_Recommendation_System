import pymysql
import numpy as np
from create_table_login_signup import login_signup

global user_logged_id

user_logged_id=login_signup()  

connection_db = pymysql.connect(host='localhost', user='root', password='root', database='moviedb')

cur = connection_db.cursor()

def create_search_history_table():
    
    cur.execute("CREATE TABLE movie_search_history(user_id INT,movie_name VARCHAR(255), genre VARCHAR(255), rating FLOAT )")

def movie_search():
    
    searching_movie= input("Enter Movie Name : ")
    
    cur.execute(f"SELECT movieid,title,genres FROM movies WHERE title LIKE '%{searching_movie}%' ")
    
    result=cur.fetchall()
    
    for res in result:
        movieid= res[0]
        title  = res[1]
        genres = res[2]
        
        cur.execute(f"SELECT rating FROM movies_rating where movieID ='{movieid}' ")
        
        ratings=cur.fetchall()
        
        ratings_list=[elem for elem in ratings]
        
        total_rating=np.mean(ratings_list)
        
        print(f"### Movie Result ### \n Movie Name : {title} \n Genre : {genres} \n Rating : {total_rating}")
        
        cur.execute(f"INSERT INTO movie_search_history(user_id ,movie_name, genre, rating  ) VALUES ('{user_logged_id}','{title}','{genres}','{total_rating}' )")   

def movie_recommendation():
    
    cur.execute(f"SELECT genre, COUNT(*) AS genre_count FROM movie_search_history WHERE user_id = '{user_logged_id}' GROUP BY genre ORDER BY genre_count DESC LIMIT 1 ")
    
    history_result=cur.fetchall()
    
    genre=history_result[0]
    
    cur.execute(f"SELECT title,genres from movies where genre = '{genre}' ")
    
    movie_list=cur.fetchall()
    
    for movie_details in movie_list:
        print(movie_details)
        
    #Rating wise and genre like movies by that user search history
    
    #Movie name likes
    
    #Year wise