from flask import Flask
from flask import render_template

from flask_wtf import CSRFProtect
from config import DevelopmentConfig

#from models import db
#from models import User

app = Flask(__name__, template_folder= "templates")
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saluda/<name>')
def saluda(name = 'Josefillo'):
    return 'Hola {}'.format(name)

@app.route('/user/<name>')
def showUser(name = 'default'):
    age = 21
    lista = [1, 2, 3, 4]
    return render_template('index.html', name = name, age = age, lista = lista, titlePage='Flask')

@app.route('/libro/<int:id>')
def getBook(id):
    return "Libro {}".format(id)

if __name__ == '__main__':
    csrf.init_app(app)
    #db.init_app(app)
    #with app.app_context()
        #db.create_all()
    HOST = app.config.get('HOST')
    PORT = int(app.config.get('PORT'))
    app.run(host=HOST, port=PORT)