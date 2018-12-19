from validation import STValidator

class dbs_datastr():
	def __init__(self):
		self.questions = [
		{
		'title': 'KewesekiHow does a water jeski move',
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
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis, odit. Beatae atque distinctio quod sequi, vitae rem accusamus vel! Itaque aut dolore qui, architecto provident doloribus beatae nam ut quod.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'
		
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

		self.postValid = STValidator()
	

	def addQuestion(self, body):
		""" This method add the new question to our datastore"""
		#set answer, posted on and answers to 0
		#validate the questions first

		if body['title'] != '' and len(body['title']) > 14:
			if len(body['tags']) != 0:
				if body['body'] != '' and len(body['body']) > 20:
					body['id'] = int(self.questions[-1]['id'] + 1)
					self.questions.append(body)
					return self.questions[-2:]
				else:
					return({"Error":"You're message cannot be smaller than 20 characters"})
			else:
				return({"Error":"Make sure to provide atleast 1 tag"})
		else:
			return({"Error": "Please ensure that  your title is larger than 14 characters"})


	def deleteQuestion(self, id):
		""" This function  deletes a question """
		for self.question in self.questions:
			if self.question['id'] == id:
				self.questions.remove(self.question)
				return self.questions


	def updateQuestions(self,id, body):
		""" This function will update a question"""

		if body['title'] != '' and len(body['title']) > 14:
			if len(body['tags']) != 0:
				if body['body'] != '' and len(body['body']) > 20:
					for self.question in self.questions:
						if self.question['id'] == id:
							self.question['title'] = body['title']
							self.question['tags'] = body['tags']
							self.question['body'] = body['body']
							# return "Updated the the questions <{}>".format(self.question['title'])
							return self.questions
							break
				else:
					return({"Error":"You're message cannot be smaller than 20 characters"})
			else:
				return({"Error":"Make sure to provide atleast 1 tag"})
		else:
			return({"Error": "Please ensure that  your title is larger than 14 characters"})

		




		
