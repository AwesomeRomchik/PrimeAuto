import sqlite3

def insertcardata():
    connection = sqlite3.connect("logindatabase.db")
    connection.execute("CREATE TABLE IF NOT EXISTS CARS(MODEL TEXT NOT NULL, YEAR TEXT, COLOUR TEXT, \
                       WORK REQUIRED TEXT, OWNER TEXT)")
    connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('Audi A5','2015','Black','Engine repair','Jimmy Hopkins'))
    connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('Opel Astra','2017','White','Manual transmission repair',
                                                             'Johnny Hendricks'))
    connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('BMW X5','2017','Red','Breaks repair','Ben Smith'))
    connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('Volkswagen Jetta','2017','Blue','Engine repair',
                                                             'Leliana Pratchett'))
    #connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('','','','',''))
    #connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('','','','',''))
    #connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('','','','',''))
    #connection.execute("INSERT INTO CARS VALUES(?,?,?,?,?)",('','','','',''))
    connection.commit()
    result = connection.execute("SELECT * FROM CARS")
    for data in result:
        print("Model: ",data[0])
        print("Year: ",data[1])
        print("Colour: ",data[2])
        print("Work: ",data[3])
        print("Owner: ",data[4])
    connection.close()

insertcardata()
    
    
