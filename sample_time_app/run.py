from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    ciurrent_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "Current Time: {}".format(ciurrent_time)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
