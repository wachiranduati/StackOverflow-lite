from flask import Flask, request
from app.api.v1.models.questions import questions

app = Flask(__name__)
app.register_blueprint(questions)


if __name__ == "__main__":
	app.run(debug=True) 