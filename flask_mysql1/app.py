import pymysql
# Membuka database connection
db = pymysql.connect("localhost", "root", "paw_flask" ) 
# Mempersiapkan sebuah cursor object menggunakan cursor()
cursor = db.cursor()
# Menjalankan query SQL menggunakan execute()
cursor.execute("SELECT VERSION()")
# Mengambil satu baris menggunakan fetchone()
data = cursor.fetchone()
print ("Database version : %s " % data)
     
# Memutuskan hubungan dengan server
db.close()