from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/test')
def test():
    with open('index.html', 'r') as f:
        data = f.read()
    return data