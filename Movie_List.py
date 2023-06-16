# -*- coding: utf-8 -*-

import pymysql

user_table = 'completed_list'

connection_db = pymysql.connect(host='localhost', user='root', password='root', database='userdb')

cur = connection_db.cursor()
def user_completed_list_table():
    # Create table if it doesn't exist
    cur.execute(f"CREATE TABLE IF NOT EXISTS {user_table} (user_name VARCHAR(25), movie_name VARCHAR(20), rating INT)")
    
    table_creation_result=cur.fetchone()
    
    if table_creation_result:
        print(f'{user_table} Table Created!!')
        connection_db.commit()
    else:
        print(f'{user_table} Table Already Created!!')
        
        
def completed_movie_list_update():
    user_logged_name=input('Enter logged user: ')
    completed_movie_name=input('Enter movie name: ')
    movie_rating=input('Enter movie rating:')

    
    cur.execute(f"SELECT * FROM {user_table} WHERE user_name = '{user_logged_name}' AND movie_name = '{completed_movie_name}'")
    
    completed_movie_result=cur.fetchone()
    
    if completed_movie_result:
        print('This movie rating existed by you! try with another moives! Thank You!')
    else:
        cur.execute(f"INSERT INTO {user_table} (user_name,movie_name,rating) VALUES ('{user_logged_name}','{completed_movie_name}','{movie_rating}')")
        print(f'{completed_movie_name} Movie Rating Updated! Thank you!')
        connection_db.commit()
        connection_db.close
        
user_completed_list_table()   
completed_movie_list_update()     
        
    