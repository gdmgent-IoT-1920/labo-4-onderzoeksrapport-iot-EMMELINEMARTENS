import sys
sys.path.insert(0,'../sensehat_board/pi')
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/sensehat')
def sensehat():
    return render_template('sensehat.html')


if __name__  == "__main__":
	app.run(host='127.0.0.1',port="8000", debug=True)