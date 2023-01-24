from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method =="POST":
        if request.form['action'] == "create":
            print("Create Game")
        else:
            game_code = request.form['game_code']
            print(f"Join game: {game_code}")
    with open('api/index.html', 'r') as f:
        data = f.read()
    return data

@app.route('/about')
def about():
    return 'About'

@app.route('/game')
def test():
    with open('api/game.html', 'r') as f:
        data = f.read()
    return data

