from flask import Flask, render_template, request
from models import UploadForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890!@#$%^&*()'
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + \
        '/UploadFile/static/uploads'
#satuan byte
app.config['MAX_CONTENT_PATH'] = 10000000

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm(request.form)
    if request.method == 'POST':
        f = request.files['file']
        filename = app.config['UPLOAD_FOLDER'] + \
            '/' + secure_filename(f.filename)
        try:
            f.save(filename)
            return render_template('upload_sukses.html')
        except:
            return render_template('upload_gagal.html')
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
