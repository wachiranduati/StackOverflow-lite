from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return('Welcome home bruh')

@app.route('/questions', methods=['GET'])
def questions():
	return('This is the questions part')

if __name__ == "__main__":
	app.run(debug=True)