# Python code written by ChatGBT when asked to write python code to interface to a Postgres Database
#
import psycopg2

class PostgresDatabase:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def query(self, query):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()
            conn.commit()
            conn.close()
            return rows
        except Exception as e:
            print(f"Error executing query: {e}")

    def insert(self, query, values):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query, values)
            cur.close()
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error executing insert statement: {e}")
