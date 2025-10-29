from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/hello")
@app.route("/pagina/<nombre>")
def pagina(nombre=None):
    return render_template('pagina.html',name = nombre)

    