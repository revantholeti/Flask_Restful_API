import sqlite3

connection = sqlite3.connect("data.db")

curser = connection.cursor()

create_query = "CREATE TABLE users(id int,username text,password text)"
curser.execute(create_query)

user = (1,'rev','rev')
insert_query = "INSERT INTO users VALUES (?,?,?)"
curser.execute(insert_query,user)

user = [
    (2,'sun','sun'),
    (3,'rio','rio')
]

curser.executemany(insert_query,user)

select_query = "SELECT * FROM users"
for row in curser.execute(select_query):
    print(row)

connection.commit()

connection.close()