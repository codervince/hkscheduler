import os
from flask import Flask,render_template,request, url_for
# https://arcane-coast-6917.herokuapp.com/ 
# https://github.com/codervince/hkscheduler
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
    # return 'Welcome to the experimental Hk raceday page!'

@app.route('/boss')
def boss():
	return render_template('boss.html')


@app.route('/form')
def form():
    return render_template('form_submit.html')

@app.route('/subscribe/', methods=['POST'])
def subscribe():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)


if __name__ == '__main__':
	app.run(debug=True)


