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
	'id': 2,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'
	
	},
	{
	'title': 'How does a water jeski move',
	'posted_on': '20HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 3,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 4,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

	
	},
	{
	'title': 'How does a water jeski move',
	'posted_on': '12HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 5,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 6,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

	
	},
	{
	'title': 'How does a water jeski move',
	'posted_on': '20HRS AGO',
	'tags': ['watersports','ocean','summer','highend','science'],
	'answers': 12,
	'id': 7,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

	
	},
	{
	'title': 'What led to the first world war?',
	'posted_on': '13HRS AGO',
	'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
	'answers': 34,
	'id': 8,
	'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'
	
	
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
	for qus in questions:
		if qus['id'] == id:
			question = qus

	return render_template('question.html', question=question)

@app.route('/question')
def question():
	return render_template('postquestions.html')


if __name__ == "__main__":
	app.run(debug=True)