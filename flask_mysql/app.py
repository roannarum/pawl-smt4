from flask import Flask, render_template,request, redirect, url_for
from models import MBukuTelepon

application = Flask(__name__)
@application.route('/')
def index():
    model = MBukuTelepon()
    container = []
    container = model.selectDB()
    return render_template('index.html', container=container)

@application.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        nama = request.form['nama']
        no_telp = request.form.get('no_telp')
        data = (nama, no_telp)
        model = MBukuTelepon()
        model.insertDB(data)
        return redirect(url_for('index'))
    else:
        return render_template('insert_form.html')

@application.route('/update/<no>')
def update(no):
    model = MBukuTelepon()
    data = model.getDBbyNo(no)
    return render_template('update_form.html', data = data)

@application.route('/update_process', methods=['GET', 'POST'])
def update_process():
    no = request.form['no']
    nama = request.form['nama']
    no_telp = request.form['no_telp']
    data = (nama, no_telp, no)
    model = MBukuTelepon()
    model.updateDB(data)
    return redirect(url_for('index'))

@application.route('/delete/<no>')
def delete(no):
    model = MBukuTelepon()
    model.deleteDB(no)
    return redirect(url_for('index'))
                  
                   
if __name__ == '__main__':
    application.run(debug=True)
            