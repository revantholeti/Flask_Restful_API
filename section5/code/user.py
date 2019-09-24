import sqlite3

class Users:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    def find_by_username(self,username):
        print(username)
        connection = sqlite3.connect("data.db")
        curser = connection.cursor()
        select_query = "SELECT * FROM users WHERE username=?"
        result = curser.execute(select_query,(username,))
        row = result.fetchone()
        print(row)
        if row:
            print(row[0],row[1],row[2])
            user = Users(row[0],row[1],row[2])
        else:
            user = None
        connection.close()

        return user
    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect("data.db")
        curser = connection.cursor()
        select_query = "SELECT * FROM users WHERE username=?"
        result = curser.execute(select_query,(_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()

        return user