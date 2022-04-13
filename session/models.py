import pymysql
import config

db = cursor = None

class MPengguna():
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def openDB(self):
        global db, cursor
        db = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        cursor = db.cursor()
    
    def closeDB(self):
        global db, cursor
        db.close()
    
    def authenticate(self):
        self.openDB()
        cursor.execute("SELECT COUNT(*) FROM pengguna WHERE username = '%s' AND password = MD5('%s')" %(self.username, self.password))
        count_account = (cursor.fetchone())[0]
        self.closeDB()
        return True if count_account>0 else False
        
