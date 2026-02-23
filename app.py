from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Félicitations !</h1><p>Bienvenue sur ma version 2.0!.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
