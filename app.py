from flask import Flask, jsonify, request
from dbs import dbs_datastr

app = Flask(__name__)
dbs_datastr = dbs_datastr()

@app.route('/',methods=['GET'])
def index():
	return('Welcome home')

@app.route('/questions', methods=['GET'])
def view_questions():
	return jsonify(dbs_datastr.questions), 200

@app.route('/questions', methods=['POST'])
def post_question():
	body = request.get_json()
	if 'success' in dbs_datastr.addQuestion(body):
		return jsonify(dbs_datastr.addQuestion(body)), 200
	else:
		return jsonify(dbs_datastr.addQuestion(body)), 300


@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
	return jsonify(dbs_datastr.deleteQuestion(id))


@app.route('/questions/<int:questionId>', methods=['PUT'])
def update_question(questionId):
	body = request.get_json()
	if 'success' in dbs_datastr.updateQuestions(questionId,body):
		return jsonify(dbs_datastr.updateQuestions(questionId,body)), 200
	else:
		return jsonify(dbs_datastr.updateQuestions(questionId,body)), 300

@app.route('/dummy')
def dummy():
	return jsonify([{'state':'success'},"Something else here"]), 200


if __name__ == "__main__":
	app.run(debug=True) 