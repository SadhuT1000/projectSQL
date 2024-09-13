import psycopg2


class  DBManager:

    def __init__(self,params):
        self.conn = psycopg2.connect(dbname='hh_db', **params)
        self.cur = self.conn.cursor()
