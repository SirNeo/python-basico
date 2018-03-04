from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder= "templates")

@app.route('/')
def index():
    return render_template('index_template.html')

@app.route('/saluda/<name>')
def saluda(name = 'Josefillo'):
    return 'Hola {}'.format(name)

@app.route('/user/<name>')
def showUser(name = 'default'):
    age = 21
    lista = [1, 2, 3, 4]
    return render_template('index_template.html', name = name, age = age, lista = lista)

@app.route('/libro/<int:id>')
def getBook(id):
    return "Libro {}".format(id)

if __name__ == '__main__':
    app.run(debug= True, port= 5001)