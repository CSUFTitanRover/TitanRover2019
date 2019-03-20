import sqlite3

class database():
    _dbname = None
    _conn = None
    _cur = None

    def __init__(self, name):
        _dbname = name
        self.create_rover_tables()

    def create_rover_tables(self):
        self.open_db()
        self._cur.execute('''CREATE TABLE IF NOT EXISTS map (
            item_id	    INTEGER PRIMARY KEY AUTOINCREMENT,
            lat	        REAL NOT NULL,
            lon      	REAL NOT NULL,
            type    	TEXT NOT NULL,
            acc_data    REAL NOT NULL
            )
            ''')
        self._cur.execute('''CREATE TABLE IF NOT EXISTS pictures (
            item_id	    INTEGER PRIMARY KEY AUTOINCREMENT,
            pict_name   TEXT NOT NULL,
            lat	        REAL NOT NULL,
            lon      	REAL NOT NULL,
            head    	REAL NOT NULL,
            servo_off   REAL NOT NULL
            )
            ''')

    def newdb(self, tablename):
        pass

    # Opens all db files and cursor attachments
    def open_db(self):
        self._conn = sqlite3.connect(self._dbname)
        self._cur = self._conn.cursor()
        # Let rows be of dict/tuple type
        self._conn.row_factory = sqlite3.Row
        print ("Opened database %s as %r" % (self._dbname, self._conn))

    # returns the size of table
    def getTableSize(self, tablename):
        return (self._dbname.execute("SELECT COUNT(*) FROM " + tablename).fetchall())[0][0]

if __name__ == "__main__":
