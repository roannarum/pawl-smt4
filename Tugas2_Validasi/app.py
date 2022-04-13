from flask import Flask, render_template, request
from models import KomentarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '@#123456&*()'

@app.route('/', methods =['GET', 'POST'])
def index():
	form = KomentarForm()
	if request.method == 'POST':
		if form.validate():
			npm = form.npm.data
			nama = form.nama.data
			email = form.email.data
			prodi = form.prodi.data
			ipk = float(form.ipk.data)
			sks = form.sks.data
			return render_template('response.html',
				npm =npm, nama=nama, email=email, 
				prodi=prodi, ipk=ipk, sks=sks)
		else:
			errors = form.errors.items()
			return render_template('form.html',
				form=form, errors=errors)

	return render_template('form.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)