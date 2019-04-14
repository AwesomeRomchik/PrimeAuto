import sqlite3

def createTable():
    #connecting to a database, if no database exists, new one is created    
    connection = sqlite3.connect("logindatabase.db")
    #specify the fields to create in the database
    connection.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME TEXT NOT NULL,PASSWORD TEXT,FULLNAME TEXT,ROLE TEXT,WORK TEXT)")
    #populating the tables
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('testing','testing','testing','mechanic','fitting'))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('stark','stark','Tony Stark','administrator',''))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('furie','furie','Jason Furie','administrator',''))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('nick','nick','Nick Fury','inspector',''))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('peterq','peterq','Peter Quill','inspector',''))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('bruce','bruce','Bruce Banner','mechanic','fitting'))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('peterp','peterp','Peter Parker','mechanic','bodyshop'))
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('eddy','eddy','Eddy Brock','mechanic','tuning'))

    #commit data to the database, otherwise not inserted
    connection.commit()
    #have the data ready
    result = connection.execute("SELECT * FROM USERS")
    for data in result:
        print("Username: ",data[0])
        print("Password: ",data[1])
        print("Full name: ",data[2])
        print("Role: ",data[3])
        print("Work type: ",data[4])
    #close connection
    connection.close()

createTable()

