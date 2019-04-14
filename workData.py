import sqlite3

def workData():
    connection = sqlite3.connect("logindatabase.db")
    connection.execute("CREATE TABLE IF NOT EXISTS BODYSHOP(WORKTYPE TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS LOCKSMITHSHOP(WORKTYPE TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS TUNING(WORKTYPE TEXT NOT NULL)")

    connection.execute("INSERT INTO BODYSHOP VALUES(?)",('Painting',))
    connection.execute("INSERT INTO BODYSHOP VALUES(?)",('Polishing',))
    connection.execute("INSERT INTO BODYSHOP VALUES(?)",('Dents corection',))
    connection.execute("INSERT INTO BODYSHOP VALUES(?)",('Part installation/removal',))

    connection.execute("INSERT INTO LOCKSMITHSHOP VALUES(?)",("Breaks repair",))
    connection.execute("INSERT INTO LOCKSMITHSHOP VALUES(?)",("Steerage repair",))
    connection.execute("INSERT INTO LOCKSMITHSHOP VALUES(?)",("Engine repair",))
    connection.execute("INSERT INTO LOCKSMITHSHOP VALUES(?)",("Gearbox repair",))

    connection.execute("INSERT INTO TUNING VALUES(?)",("Cabin sewing",))
    connection.execute("INSERT INTO TUNING VALUES(?)",("Noise cancellation",))

    connection.commit()

    result = connection.execute("SELECT * FROM BODYSHOP")
    for data in result:
        print("Worktype bodyshop: ", data[0])

    result2 = connection.execute("SELECT * FROM LOCKSMITHSHOP")
    for data2 in result2:
        print("Worktype locksmithshop: ", data2[0])

    result3 = connection.execute("SELECT * FROM TUNING")
    for data3 in result3:
        print("Worktype tuning: ", data3[0])

workData()


