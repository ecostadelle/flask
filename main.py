from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Olá mundo!"

@app.route('/<val>')

def previsao(val):
    return val

app.run(port=80)
