from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    usuario = {"nome":"Emilly", "sobrenome":"Natacha"}
    return render_template('index.html', usuario=usuario, titulo='Página Inicial')

@app.route('/outro')
def outro():
    return render_template('contato.html', titulo= "Contato")