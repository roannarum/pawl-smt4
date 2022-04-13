from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, RadioField
#from wtforms.validators import Required, Length, Email, URL

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