from flask import Flask, jsonify, request
from dbs import dbs_datastr

app = Flask(__name__)
dbs_datastr = dbs_datastr()

@app.route('/',methods=['GET'])
def index():
	return('Welcome home bruh')

@app.route('/questions', methods=['GET'])
def view_questions():
	return jsonify(dbs_datastr.questions)

@app.route('/questions', methods=['POST'])
def post_question():
	body = request.get_json()
	# dbs_datastr.questions
	pass

if __name__ == "__main__":
	app.run(debug=True)