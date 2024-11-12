import mysql.connector

#create database cinnection  to mysql
connection = mysql.connector.connect(host = "localhost",
                                      username = "root",
                                      password = "Prince@2006",
                                      database = "event")

#to check the connection establish or not
if connection.is_connected():
    print("db is connected")
else:
    print("db not connected")
#to create user table in database
users = "create table if not exists addevent(eventname text, username text, eventdate text, email text,department text, mobile text)"

#to pass there cursor handle sql query
mycursor = connection.cursor()

#to execute the sql query
mycursor.execute(users)
connection.commit()

#to insert fname in users table
insertName = "insert into addevent value('{}','{}','{}','{}','{}','{}')".format(input("Enter Event Name:"),input("Enter User Name:"),input("Enter Event Date: "),input("Enter Gmail: "),input("Enter Student Department: "),input("Enter Mobile No.: "))
mycursor.execute(insertName)
connection.commit()

#to update the event details in database
updateEvent = "update addevent set eventname = 'VAM' where mobile = '0987654321'"
mycursor.execute(updateEvent)
connection.commit()