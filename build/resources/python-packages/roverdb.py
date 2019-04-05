import sqlite3

class Database():
    _dbname = 'rover.sqlite3'
    _cur = None
    _conn = None

    def __init__(self):
        #_dbname = str('rover.sqlite3')
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
        self.close_db()

    # Opens all db files and cursor attachments
    def open_db(self):
        self._conn = sqlite3.connect(self._dbname)
        self._cur = self._conn.cursor()
        # Let rows be of dict/tuple type
        #self._conn.row_factory = sqlite3.Row
        print ("Opened database %s as %r" % (self._dbname, self._conn))

    def close_db(self):
        self._conn.commit()
        self._conn.close()

    def insertMap(self, table_name, value1 = 0, value2 = 0, value3 = 0, value4 = 0):
        self.open_db()
        self._cur.execute('''INSERT INTO map (lat, lon, type, acc_data) VALUES(?, ?, ?, ?)''', (value1, value2, value3, value4)) 
        self.close_db()

    # returns the size of table
    def getTableSize(self, tablename):
        self.open_db()
        total = (self._cur.execute("SELECT COUNT(*) FROM " + tablename).fetchall())[0][0]
        self.close_db()
        return total

    def getAccelValue(self, lat, lon):
        self.open_db()
        lookup = 'SELECT lat, lon, acc_data FROM map WHERE lat =' + str(lat) + ' AND lon = ' + str(lon)
        val = self._cur.execute(lookup)
        found = val.fetchone()[2]
        self.close_db()
        if found:
            return found
        else:
            return 0
    
if __name__ == '__main__':
    # Testing the file
    dbexist = True
    if not dbexist:
        db = Database()
        db.insertMap(map,34.43443, -117.23243,'primary', -3.44)
        print(db.getAccelValue(34.43443, -117.23243))
    else:
        pass
