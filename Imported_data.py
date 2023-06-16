#Data Import into DB
import pandas as pd
import pymysql

print('Movie Recommendation System\n')

def create_movie_db():
    connection_db = pymysql.connect(
            host='localhost',
            user='root', 
            password = "root",
            )
          
    cur = connection_db.cursor()
      
    # Select query
    cur.execute("create database moviedb")
    moviedb_creation_res=cur.fetchone()
    
    if moviedb_creation_res:
        print('movie_db created successfully!')
    else:
        print('movie_db already created!')
    # To close the connection
    connection_db.close()

def tables_creation_data_import():
    connection_db = pymysql.connect(
            host='localhost',
            user='root', 
            password = "root",
            database='moviedb'
            )
          
    cur = connection_db.cursor()
    

    cur.execute("create table movies(movieid int ,title varchar(255), genres varchar(255))")
    movie_table_res=cur.fetchone()
    
    if movie_table_res:
        print(f'table table created successfully!')
    else:
        print(f'table already created!')
        
    cur.execute("create table movies_rating(userID int,movieID varchar(255), rating FLOAT, timestamp DATETIME)")
    
    rating_table_res=cur.fetchone()
    
    if rating_table_res:
        print(f'table table created successfully!')
    else:
        print(f'table already created!')
    
    movie=pd.read_csv('D:/DS/Task/movie recommendation system/Extracted_CSV/movie.csv')
    rating=pd.read_csv('D:/DS/Task/movie recommendation system/Extracted_CSV/rating.csv')
    
    
    movie_data = movie.to_records(index=False)
    rating_data = rating.to_records(index=False)
    
    movie_sql = "INSERT INTO movies (movieid, title, genres) VALUES (%s, %s, %s)"
    rating_sql = "INSERT INTO movies_rating (userID, movieID, rating,timestamp) VALUES (%s, %s, %s,%s)"
    
    for row1 in movie_data:
        cur.execute(movie_sql, tuple(row1))
    
    for row in rating_data:
        cur.execute(rating_sql, tuple(row))
    connection_db.commit()    
    # To close the connection
    connection_db.close()
    
#create_movie_db()    
tables_creation_data_import()
