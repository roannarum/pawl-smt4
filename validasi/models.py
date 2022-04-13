from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
#from wtforms.validators import Required, Length, Email, URL

class KomentarForm(FlaskForm):
	nama = StringField('Nama:',
		validators=[validators.DataRequired('Nama harus diisi!'),
		validators.Length(max=25)])
	email = StringField('Email:',
		validators=[validators.DataRequired('Email harus diisi!'),
		validators.Email('Alamat email tidak ditulis dengan benar.')])
	url = StringField('URL:',
		validators=[validators.DataRequired('URL harus diisi!'), validators.URL()])
	komentar = TextAreaField('Komentar',
		validators=[validators.DataRequired('Komentar harus diisi!')])
	submit = SubmitField('Kirim')