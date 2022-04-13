from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    poto = [
        {
            'nama' : '1. Kim Junkyu',
            'image': 'images/img7.jpg'
        },
        {
            'nama' : '2. Haruto',
            'image': 'images/img2.jpg'
        },
        {
            'nama' : '3. Haruto 2',
            'image': 'images/img3.jpg'
        },
        {
            'nama' : '4. Treasure',
            'image': 'images/img4.jpg'
        },
        {
            'nama' : '5. Treasure',
            'image': 'images/img5.jpg'
        }
    ]
  
    return render_template('index.html',poto=poto)
if __name__ == '__main__':
    application.run(debug=True)