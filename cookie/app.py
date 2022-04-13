
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    var = 100
    msg = 'Cookie "var" telah dibuat'
    response = make_response(render_template('index.html', msg=msg))
    response.set_cookie("var", str(var))
    return response

@app.route('/ubahCookie')
def ubahCookie():
    var = 200
    msg = 'Cookie "var" telah diubah'
    response = make_response(render_template('index.html', msg=msg))
    response.set_cookie("var", str(var))
    return response

@app.route('/hapusCookie')
def hapusCookie():
    msg = 'Cookie "var" telah dihapus'
    response = make_response(render_template('index.html', msg=msg))
    response.set_cookie("var", '', expires=0)
    return response

@app.route('/halaman1')
def halaman1():
    var = request.cookies.get("var")
    return render_template('halaman1.html', var=var)

@app.route('/halaman2')
def halaman2():
    var = request.cookies.get("var")
    return render_template('halaman2.html', var=var)

if __name__ == '__main__':
    app.run(debug=True)