import mariadb
import sys
import re
from collections import defaultdict
from params import Params

class Sql:

    def __init__(self):
        self.Params = Params().descbb
        self.conn = self.create_connection()
        self.cur = self.conn.cursor()
        self.tables = self.get_tables()

    def reset(self):
        try:
            self.cur.execute('TRUNCATE TABLE statsbb')
            self.conn.commit()
            return 'reset'
        except mariadb.Error as e:
            return 'reset error ' + e
        # if self.sql_query('TRUNCATE TABLE statsbb'):
        #     return 'TRUNCATE TABLE statsbb'
        # else:
        #     return 'Non TRUNCATE TABLE statsbb'

    def action(self, data):
        if self.check_table():
            self.addSql(data)
        else:
            self.createTable()
            self.addSql(data)
        self.close_connect()

    def get_top_coin_indicators(self):
        nesteddict = lambda: defaultdict(nesteddict)
        resDic = nesteddict()
        statsbb = self.sql_query(
            'SELECT * FROM statsbb WHERE cast(volume as unsigned) > 10000 ORDER BY cast(macd as unsigned) DESC')
        n = 0
        listCoinLen = len(Params().descbb)
        for val in statsbb:
            k = 0
            while k < listCoinLen:
                resDic[n][Params().descbb[k]] = val[k]
                k += 1
            n += 1

        return resDic

    def create_connection(self):
        try:
            self.conn = mariadb.connect(
                user="bb",
                password="bb111!",
                host="localhost",
                database="statsbb",
                port=3306)
            print("Connect maria db base statsbb")
            return self.conn

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def close_connect(self):
        self.conn.close()
        print("Close mariadb connection")

    def get_tables(self):
        ar = []
        for tablenamebase in self.sql_query("SHOW TABLES"):
            ar.append(re.sub('[^a-zA-Z0-9]', '', str(tablenamebase)))
        return ar

    def sql_query(self, query):
        self.cur.execute(query)
        ar = []
        for databasename in self.cur:
            ar.append(databasename)

        return ar

    def check_table(self):
        return 'statsbb' in self.tables

    def addSql(self, data):
        query = "INSERT INTO statsbb ("
        queryCol = ""
        queryVal = ""
        for col in data:
            queryCol += col + ", "
            queryVal += '"' + data[col] + '", '

        query += queryCol[:-2] + ") VALUES (" + queryVal[:-2] + ")"
        self.cur.execute(query)
        self.conn.commit()
        return self.cur

    def createTable(self):
        query = "CREATE TABLE statsbb ("
        for col in self.Params:
            query += col + ' varchar(255), '

        query = query[:-2] + ")"

        self.cur.execute(query)
        return self.cur





