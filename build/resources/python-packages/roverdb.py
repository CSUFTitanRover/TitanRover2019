import sqlite3

class Database():
    _dbname = "db.sql"
    _cur = None
    _conn = None

    def __init__(self):
        _dbname = "rover"
        # self.create_rover_tables() Only needs to run on first call

    def create_rover_tables(self):
        self.open_db(self)
        self._cur.execute('''CREATE TABLE IF NOT EXISTS map (
            item_id	    INTEGER PRIMARY KEY AUTOINCREMENT,
            lat	        REAL NOT NULL,
            lon      	REAL NOT NULL,
            type    	TEXT NOT NULL,
            acc_data    REAL
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

    def insert(self, value, table_name):
        self.open_db()
        self._cur.execute('''INSERT INTO map (lat, lon, type, acc_data) VALUES(?, 0, 0, 0)''', (value,))
        self._conn.close()

    def insert(self,value1,value2,table_name):
        self.open_db()
        self._cur.execute('''INSERT INTO map (lat, lon, type, acc_data) VALUES(?, ?, '0', 0)''', (value1,value2,))
        self._conn.close()

    # Opens all db files and cursor attachments
    def open_db(self):
        self._conn = sqlite3.connect(str(self._dbname))
        self._cur = self._conn.cursor()
        # Let rows be of dict/tuple type
        self._conn.row_factory = sqlite3.Row
        print ("Opened database %s as %r" % (self._dbname, self._conn))


    # returns the size of table
    def getTableSize(self, tablename):
        return (self._cur.execute("SELECT COUNT(*) FROM " + tablename).fetchall())[0][0]


