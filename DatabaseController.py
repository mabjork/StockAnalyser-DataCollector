
import psycopg2

class DatabaseController(object):

    def __init__(self):
        try:
                self.connection = psycopg2.connect("dbname='testdb' user='postgres_user' host='localhost' password='123'")
                self.connected = true
        except:
                print "I am unable to connect to the database"
                self.connected = false

    def saveToDB(self,data):
        if not(self.connected):
            print "Not connected to database"
            return
        if not(checkIfIdExists(data[0]["stock_id"])):
            cur = self.connection.cursor()
            cur.executemany("""INSERT INTO stock(id,name,symbol,sector) VALUES (%(stock_id)s ,%(name)s, %(symbol)s, %(sector)s)""", data)
            self.connection.commit()
        else:
            print "Id already exists"

    def checkIfIdExists(self,stock_id):
        data = []
        data.append(stock_id)
        cur = self.connection.cursor()
        cur.execute("""SELECT * from stock where id = %s""",data)
        for item in cur:
            return True
        return False
