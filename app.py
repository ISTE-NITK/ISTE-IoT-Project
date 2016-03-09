from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about/')
def cakes():
    return 'A Project by ISTE- NITK Chapter.'

@app.route('/hello/<name>/')
def hello(name):
	return render_template('page.html', name=name)

if __name__ == '__main__':
	app.run(debug=True, host= '0.0.0.0', port=int("8000"))