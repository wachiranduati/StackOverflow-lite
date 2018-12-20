from flask import Blueprint, jsonify, request
from dbs import dbs_datastr


questions = Blueprint('questions', __name__)
dbs_datastr = dbs_datastr()


@questions.route('/',methods=['GET'])
def index():
	return('Welcome home')

@questions.route('/questions', methods=['GET'])
def view_questions():
	return jsonify(dbs_datastr.questions), 200

@questions.route('/questions', methods=['POST'])
def post_question():
	body = request.get_json()
	if 'success' in dbs_datastr.addQuestion(body):
		return jsonify(dbs_datastr.addQuestion(body)), 200
	else:
		return jsonify(dbs_datastr.addQuestion(body)), 300


@questions.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
	return jsonify(dbs_datastr.deleteQuestion(id))


@questions.route('/questions/<int:questionId>', methods=['PUT'])
def update_question(questionId):
	body = request.get_json()
	if 'success' in dbs_datastr.updateQuestions(questionId,body):
		return jsonify(dbs_datastr.updateQuestions(questionId,body)), 200
	else:
		return jsonify(dbs_datastr.updateQuestions(questionId,body)), 300

@questions.route('/dummy')
def dummy():
	return jsonify([{'state':'success'},"Something else here"]), 200