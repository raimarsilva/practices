from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/time')
def show_time():
    text = input('Enter the time: ')
    return '<h2>Hora: '+text+'</h2>'