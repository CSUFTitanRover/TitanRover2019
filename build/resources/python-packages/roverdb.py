import sqlite3

class Database():
    _dbname = '/home/skrapmi/TitanRover2019/slam/rover.sqlite3'
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
        #print ("Opened database %s as %r" % (self._dbname, self._conn))

    def close_db(self):
        self._conn.commit()
        self._conn.close()

    def insertMap(self, table_name, lat = 0, lon = 0, gps_type = 0, accel = 0):
        #self.open_db()
        if self.getAccelValue(lat, lon) == 0:
            self.open_db()
            self._cur.execute('''INSERT INTO map (lat, lon, type, acc_data) VALUES(?, ?, ?, ?)''', (lat, lon, gps_type, accel)) 
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
        try:
            found = val.fetchone()[2]
            self.close_db()
            return found
        except TypeError as e:
            self.close_db()
            return 0

    def getLatLonValue(self, item_id):
        try:
            self.open_db()
            lookup = 'SELECT lat, lon FROM map WHERE item_id =' + str(item_id)
            val = self._cur.execute(lookup)
            coords = val.fetchall()
            self.close_db()
            return coords[0]
        except TypeError as e:
            self.close_db()
            return 0, 0


    def updateMapAccel(self, lat, lon, Accel):
        self.open_db()
        lookup = 'SELECT item_id, lat, lon, acc_data FROM map WHERE lat =' + str(lat) + ' AND lon = ' + str(lon)
        val = self._cur.execute(lookup)
        try:
            found = val.fetchone()[0] 
            self._cur.execute('UPDATE map SET acc_data = ' + str(Accel) + ' WHERE item_id = ' + str(found))
            self.close_db()
            return found
        except TypeError as e:
            self.close_db()
            return 0


# This class is ment for import design test scripts are below and do not affect imports
if __name__ == '__main__':
    # Testing the file
    dbexist = True
    
    if not dbexist:
        db = Database()
        db.insertMap(map,50.47643, -117.23244,'primary', -3.44)
        print(db.updateMapAccel(50.47643, -117.23244, 5.0))
    else:
        db = Database()
        print(db.getLatLonValue(5))
        pass
