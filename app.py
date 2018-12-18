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
	return jsonify(dbs_datastr.addQuestion(body))

@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
	return jsonify(dbs_datastr.deleteQuestion(id))


@app.route('/questions/<int:questionId>', methods=['PUT'])
def update_question(questionId):
	body = request.get_json()
	return jsonify(dbs_datastr.updateQuestions(questionId,body))


if __name__ == "__main__":
	app.run(debug=True) 