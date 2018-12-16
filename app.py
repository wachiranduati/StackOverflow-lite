from flask import Flask, render_template
import datetime, re

app = Flask(__name__)

#ans,tags,title,
#time 2017-10-17 23:48:55
questions = [
	{
	'title': 'How does a water jeski move',
	'posted_on': '12HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 1,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat adipisci, officiis cumque, commodi dicta cum possimus! Et, aliquam. Doloremque doloribus atque numquam quod qui in sapiente quibusdam earum, sit quas!'
	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 2
	
	},
	{
	'title': 'How does a water jeski move',
	'posted_on': '20HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 3
	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 4
	
	},
	{
	'title': 'How does a water jeski move',
	'posted_on': '12HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 5
	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 6
	
	},
	{
	'title': 'How does a water jeski move',
	'posted_on': '20HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 7
	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 8
	
	}
]

@app.route('/')
def home():
	return render_template('index.html', questions=questions)

@app.route('/signup')
def signup():
	return render_template('createaccount.html')

@app.route('/signin')
def signin():
	return render_template('loginaccount.html')

@app.route('/question/<question>/<int:id>')
def view_question(question, id):
	return render_template('question.html')

@app.route('/question')
def question():
	return render_template('postquestions.html')


if __name__ == "__main__":
	app.run(debug=True)