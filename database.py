import sqlite3 as sql
# create database
con = sql.connect('login.db')

# create cursor to execute sql commands
cur = con.cursor()

# created login table that holds username and pass
# next 5 lines are commented out because the table is already created and cant be created twice

# cur.execute("""CREATE TABLE loginDetails (
#     username text,
#     email blob,
#     password integer
#     )""")

# adding data
# next line is commented out because you need it to be commented out to view the data.

# cur.execute("INSERT INTO loginDetails VALUES ('unlqsting', 'noorbijapur500@gmail.com', 123)")

# view added data
cur.execute("SELECT * FROM loginDetails")
print(cur.fetchall())

# commits the current data
con.commit()

# closes connection to db
con.close()

