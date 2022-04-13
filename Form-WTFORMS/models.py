from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, BooleanField, SubmitField

class PersonalForm(FlaskForm):
      nama = StringField('Nama:')
      alamat = TextAreaField('Alamat:') 
      jeniskelamin = RadioField ('Jenis Kelamin:',
            choices=[('P','Pria'),('W', 'Wanita')])
                  
      agama = SelectField('Agama:',
      choices=[
            (1, 'Islam'),
            (2, 'Protestan'),
            (3, 'Katolik'),
            (4, 'Hindu'),
            (5, 'Budha')
            ])
      hobi1 = BooleanField('Olahraga')
      hobi2 = BooleanField('Membaca')
      hobi3 = BooleanField('Jalan-Jalan')
      submit = SubmitField('Kirim')



