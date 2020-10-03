from flask import Flask #, flash
from flask import render_template #, jsonify, request, redirect, url_for

app = Flask(__name__)

lista = [['juan', 'pepe'], ['ana', 'gonzalez'], ['maria', 'ramos'], ['esteban', 'sosa'], ['cluadia','alvarez']]


@app.route('/')
def index():
    return render_template('/index.html', personas = lista)

@app.route('/about')
def about():
    return 'about section of my page'


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)