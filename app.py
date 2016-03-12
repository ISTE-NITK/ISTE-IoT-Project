from flask import Flask, render_template,request 

app = Flask(__name__)

@app.route('/')											#by default this can  handle only GET methods, we need to declare POST if we need (form submissions)
def index():
	return render_template('index.html')

@app.route('/about/')
def about():
    return 'A Project by ISTE- NITK Chapter.'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    	return 'You are using POST'
    else:
    	return 'You are probably using GET'

@app.route('/hello/<name>/')							#name is the variable we pass to this route 
def hello(name):
	return render_template('page.html', name=name) 		#pass name variable to page.html Why is it left to right association? 

if __name__ == '__main__':
	app.run(debug=True, host= '0.0.0.0', port=int("8000"))