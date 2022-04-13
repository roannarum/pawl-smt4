import pymysql
import config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, RadioField

db = cursor = None

class Mahasiswa:
    def __init__(self, no=None, npm=None, nama=None, prodi=None, ipk=None, sks=None):
        self.no = no
        self.npm = npm
        self.nama = nama
        self.prodi = prodi
        self.ipk = ipk
        self.sks = sks
    def openDB(self):
        global db, cursor
        db = pymysql.connect(
                host=config.DB_HOST,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database=config.DB_NAME)
        cursor = db.cursor()
           
    def closeDB(self):
        global db, cursor
        db.close()
    
    def selectDB(self):
        self.openDB()
        cursor.execute("SELECT * FROM mahasiswa")
        container = [] 
        for no, npm, nama, prodi, ipk, sks in cursor.fetchall():
            container.append((no, npm, nama, prodi, ipk, sks))
        self.closeDB()
        return container
    
    def insertDB(self, data):
        self.openDB()
        cursor.execute(
            "INSERT INTO mahasiswa (npm, nama, prodi, ipk, sks) VALUES('%s', '%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()


class KomentarForm(FlaskForm):
    npm = StringField('NPM: ',
        validators=[validators.DataRequired('NPM harus diisi!'),
		validators.Length(max=9)])
    nama = StringField('Nama:',
		validators=[validators.DataRequired('Nama harus diisi!'),
		validators.Length(max=25)])
    email = StringField('Email:',
		validators=[validators.DataRequired('Email harus diisi!'),
		validators.Email('Alamat email tidak ditulis dengan benar.')])
    prodi = RadioField('Prodi: ',
        choices=[('Sistem Informasi', 'Sistem Informasi'),
        ('Teknologi Informasi', 'Teknologi Informasi'),
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Teknik Industri', 'Teknik Industri')],
        validators=[validators.DataRequired('Prodi!')])
    ipk = StringField('IPK:',
	    validators=[validators.DataRequired('IPK harus diisi!')])
    sks = StringField('SKS',
		validators=[validators.DataRequired('SKS harus diisi!')])
    submit = SubmitField('Kirim')
