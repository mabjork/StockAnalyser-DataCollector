
import psycopg2

class DatabaseController(object):

    def __init__(self):
        try:
                self.connection = psycopg2.connect("dbname='testdb' user='postgres' host='localhost' password='1234'")
                self.connected = True
        except:
                print("I am unable to connect to the database")
                self.connected = False

    def saveToDB(self,data):
        if not(self.connected):
            print("Not connected to database")
            return
        if not(self.checkIfIdExists("stock",data[0]["stock_id"])):
            cur = self.connection.cursor()
            cur.executemany("""INSERT INTO stock(id,name,symbol,sector) VALUES (%(stock_id)s ,%(name)s, %(symbol)s, %(sector)s)""", data)
            self.connection.commit()
        else:
            print "Id already exists"

    def savePCurrencyToDB(self,data):
        if not(self.connected):
            print "Not connected to database"
            return
        if not(self.checkIfIdExists("physical_currencies",data[0]["id"])):
            cur = self.connection.cursor()
            cur.executemany("""INSERT INTO physical_currencies(id,name,symbol) VALUES (%(id)s ,%(name)s, %(symbol)s)""", data)
            self.connection.commit()
        else:
            print "Id already exists"

    def saveDCurrencyToDB(self,data):
        if not(self.connected):
            print "Not connected to database"
            return
        if not(self.checkIfIdExists("digital_currencies",data[0]["id"])):
            cur = self.connection.cursor()
            cur.executemany("""INSERT INTO digital_currencies(id,name,symbol) VALUES (%(id)s ,%(name)s, %(symbol)s)""", data)
            self.connection.commit()
        else:
            print "Id already exists"

    def checkIfIdExists(self,table,entity_id):
        data = []
        data.append(entity_id)
        cur = self.connection.cursor()
        cur.execute("""SELECT * from """ +table+""" where id = %s""",data)
        
        for item in cur:
            return True

        return False
    
    
