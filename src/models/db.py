'''import mysql-


class DbConn(object):
    def __init__(self):
        self.conn = sqlite3.connect('app.db')
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        # type: () -> sqlite3.connect().cursor()
        self.conn = sqlite3.connect('app.db')
        self.cursor = self.conn.cursor()
        return self.cursor

    def close(self):
        self.conn.close()


db = DbConn()


def query_db(sql, param=()):
    cursor = db.get_cursor()
    try:
        query = cursor.execute(sql, param).fetchall()
    except(sqlite3.OperationalError):
        raise sqlite3.OperationalError
    cursor.close()
    db.conn.commit()
    db.close()
    return query

'''