from flask import Flask, render_template,request
from models import Mahasiswa
from models import KomentarForm

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'
@application.route('/hasil',methods=['GET', 'POST'])
def index():
    model = Mahasiswa()
    container = []
    container = model.selectDB()
    return render_template('data.html', container=container)

@application.route('/', methods=['GET', 'POST'])
def insert():
    form = KomentarForm()
    if request.method == 'POST':
        if form.validate():
            npm = form.npm.data
            nama = form.nama.data
            prodi = form.prodi.data
            ipk = float(form.ipk.data)
            sks = form.sks.data
            obj = (npm,nama,prodi,ipk,sks)
            model = Mahasiswa()
            container = []
            model.insertDB(obj)
            container = model.selectDB()
            return render_template('response.html', npm=npm, 
            nama=nama, prodi=prodi, ipk=ipk, sks=sks, 
            form=form,container=container)
        else:
            errors = form.errors.items()
            return render_template('form.html',	form=form, 
            errors=errors)

    return render_template('form.html', form=form)

               
if __name__ == '__main__':
    application.run(debug=True)
            