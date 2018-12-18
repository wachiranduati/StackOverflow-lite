from flask import Flask, jsonify
from dbs import dbs_datastr

app = Flask(__name__)
dbs_datastr = dbs_datastr()

@app.route('/',methods=['GET'])
def index():
	return('Welcome home bruh')

@app.route('/questions', methods=['GET'])
def questions():
	# return('This is the questions part')
	return jsonify(dbs_datastr.questions)

if __name__ == "__main__":
	app.run(debug=True)