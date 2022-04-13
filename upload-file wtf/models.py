from flask_wtf import Form
from wtforms import FileField, SubmitField

class UploadForm(Form):
    file = FileField('Pilih file yang akan diunggah:') 
    submit = SubmitField('Upload')