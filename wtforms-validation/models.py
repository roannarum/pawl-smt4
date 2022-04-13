from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length, Email, URL


class KomentarForm(FlaskForm):
    nama = StringField('Nama:',
        validators=[Required('Nama harus diisi!'),
        Length(max=25)])

    email = StringField('Email:',
        validators=[Required('Email harus diisi!'),
        Email('Alamat email tidak ditulis dengan benar.')])

    url = StringField('URL:',
        validators=[Required('URL harus diisi!'), URL()])

    komentar = TextAreaField('Komentar', 
        validators=[Required('Komentar harus diisi!')])

    submit = SubmitField('Kirim')

# https://stackabuse.com/flask-form-validation-with-flask-wtf/