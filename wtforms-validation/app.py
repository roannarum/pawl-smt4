from flask import Flask, render_template, request
from models import KomentarForm

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'


@application.route('/', methods =['GET', 'POST'])
def index():
    form = KomentarForm()
    if request.method == 'POST':
        # melakukan validasi data di dalam form
        if form.validate():
            nama = form.nama.data 
            email = form.email.data 
            url = form.url.data 
            komentar = form.komentar.data
            return render_template('response.html',
                nama=nama, email=email,
                url=url, komentar=komentar)
        else:
            # mengambil daftar kesalahan yang muncul
            # pada saat proses validasi
            errors = form.errors.items()
            return render_template('form.html',
                form=form, errors=errors)

    return render_template('form.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)