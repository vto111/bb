import mariadb
import sys
import re

class Sql:

    def __init__(self, criptopara):
        self.data = criptopara
        self.conn = self.create_connection()
        self.cur = self.conn.cursor()
        self.tables = self.get_tables()
        self.action()

    def create_connection(self):
        try:
            self.conn = mariadb.connect(
                user="bb",
                password="bb111!",
                host="localhost",
                database="statsmacd",
                port=3306)
            print("Connect maria db base statsmacd")
            return self.conn

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def close_connect(self):
        self.conn.close()
        print("Close mariadb connection")

    def get_tables(self):
        ar = []
        for tablenamebase in self.get_select("SHOW TABLES"):
            ar.append(re.sub('[^a-zA-Z0-9]', '', str(tablenamebase)))
        return ar

    def get_select(self, query):
        self.cur.execute(query)
        ar = []
        for databasename in self.cur:
            ar.append(databasename)

        return ar

    def check_table(self):
        return self.data[0] in self.tables

    def addSql(self):
        query = "INSERT INTO " + self.data[0] + " (" + self.data[1] + ", " + self.data[3] + ") VALUES (" + self.data[2] + ", " + self.data[4] + ")"
        self.cur.execute(query)
        self.conn.commit()
        return self.cur

    def createTable(self):
        self.cur.execute("CREATE TABLE " + self.data[0] + "(" + self.data[1] + " varchar(255), " + self.data[3] + " varchar(255))")
        return self.cur

    def action(self):
        if self.check_table():
            self.addSql()
        else:
            self.createTable()
            self.addSql()
        self.close_connect()



