import pymysql

print('#########Login/Signup#########')

user_table = 'users_lists'

connection_db = pymysql.connect(host='localhost', user='root', password='root', database='userdb')

cur = connection_db.cursor()

def table_creation():
    # Create table if it doesn't exist
    cur.execute(f"CREATE TABLE IF NOT EXISTS {user_table} (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(25), password VARCHAR(20))")
    connection_db.commit()
    table_creation_result=cur.fetchone()
    if table_creation_result:
        print(f'{user_table} Table Created!!')
    else:
        print(f'{user_table} Table Already Created!!')
    
def login_signup():
    user_name = input('Enter User Name: ')
    user_password = input('Enter Password: ')
    
    cur.execute(f"SELECT * FROM {user_table} WHERE name = '{user_name}' AND password = '{user_password}'")
    
    result = cur.fetchone()
    user_looged=user_name
    if result:
        print('Login Successful!!')
        
    else:
        cur.execute(f"INSERT INTO {user_table} (name, password) VALUES ('{user_name}', '{user_password}')")
        print('Username and password registered. Login successful!')
        
    
    # To close the connection
    connection_db.commit()
    connection_db.close()
    return user_looged
    
    
table_creation()
login_signup()