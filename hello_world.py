from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/cc/<text>')
def cc(text):
    return str(len(text)) + " characters!"

@app.route('/random/<fr>/<to>')
def random(fr, to):
    import random
    try:
        return str(random.randint(int(fr), int(to)))
    except:
        return "ERROR"
