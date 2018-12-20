from flask import json
import unittest
import os
from run import app

class TestSTackAPI(unittest.TestCase):
	def setUp(self):
		# self.app = create_app(config_name="Testing")
		# self.client = self.app.test_Client()
		self.question = {
		'title': 'What led to the first world war?',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}

	def test_get_questions(self):
		""" This function checks to see whether the the respond is a http 200 response"""
		self.response_message = app.test_client().get('/questions')
		self.assertEqual(self.response_message.status_code, 200)

	def test_post_question(self):
		""" This function ensures the reponse is responds correcly with a successfull post"""
		self.response_message = app.test_client().post('/questions',
			data=json.dumps(self.question),
			content_type="application/json")

		self.assertEqual(self.response_message.status_code, 200)
		self.response_msg = json.loads(self.response_message.data.decode('UTF-8'))
		self.assertEqual("success", self.response_msg[-1])

	def test_post_fail_short_title(self):
		""" Thsi method checks for successful failure via short title supplied"""
		self.response_message = app.test_client().post('/questions',
			data = json.dumps({
		'title': 'What led',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("Please ensure that  your title is larger than 14 characters", self.response_msg['Error'])

	def test_post_fail_empty_title(self):
		""" This method checks for successful failure via empty title supplied """
		self.response_message = app.test_client().post('/questions',
			data = json.dumps({
		'title': '',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("Please ensure that  your title is larger than 14 characters", self.response_msg['Error'])

	def test_post_fail_empty_tags(self):
		""" This method checks for a successful failure by not providing tags"""
		self.response_message = app.test_client().post('/questions',
			data = json.dumps({
		'title': 'Obviously theres quite some content on this title right',
		'posted_on': '13HRS AGO',
		'tags': [],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("Make sure to provide atleast 1 tag", self.response_msg['Error'])


	def test_post_fail_empty_body(self):
		self.response_message = app.test_client().post('/questions',
			data = json.dumps({
		'title': 'Obviously theres quite some content on this title right',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': ''

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("You're message cannot be smaller than 20 characters", self.response_msg['Error'])


	def test_dummy_data(self):
		response_message = app.test_client().get("/dummy",
			data=json.dumps(self.question),
			content_type="application/json")
		self.assertEqual(response_message.status_code,200)
		self.response_msg = json.loads(response_message.data.decode("UTF-8"))
		self.assertEqual("success",self.response_msg[0]['state'])

	def test_update_question(self):
		""" This function ensures the reponse is responds correcly with a successfull post"""
		self.response_message = app.test_client().put('/questions/3',
			data=json.dumps(self.question),
			content_type="application/json")

		self.assertEqual(self.response_message.status_code, 200)
		self.response_msg = json.loads(self.response_message.data.decode('UTF-8'))
		self.assertEqual("success", self.response_msg[-1])

	def test_update_fail_short_title(self):
		""" Thsi method checks for successful failure via short title supplied"""
		self.response_message = app.test_client().put('/questions/3',
			data = json.dumps({
		'title': 'What led',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("Please ensure that  your title is larger than 14 characters", self.response_msg['Error'])

	def test_update_fail_empty_title(self):
		""" This method checks for successful failure via empty title supplied """
		self.response_message = app.test_client().put('/questions/3',
			data = json.dumps({
		'title': '',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("Please ensure that  your title is larger than 14 characters", self.response_msg['Error'])

	def test_update_fail_empty_tags(self):
		""" This method checks for a successful failure by not providing tags"""
		self.response_message = app.test_client().put('/questions/3',
			data = json.dumps({
		'title': 'Obviously theres quite some content on this title right',
		'posted_on': '13HRS AGO',
		'tags': [],
		'answers': 34,
		'id': 8,
		'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro vitae placeat vel adipisci tenetur deleniti fugiat laborum beatae natus, sint necessitatibus! Deserunt adipisci ipsam quam voluptatem corporis, saepe perferendis nulla.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia, nihil reprehenderit nisi doloribus explicabo, porro tenetur sunt nulla eveniet atque. Cupiditate necessitatibus tempora consequuntur ea totam itaque, id fugiat libero.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus perspiciatis cum quis tenetur esse distinctio, officiis libero, numquam neque quas, blanditiis ad, officia exercitationem minus illum quos! Eveniet, culpa, delectus?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur qui dolor sit cupiditate expedita vitae, provident sint culpa ipsum ad minima nulla, explicabo labore numquam voluptatibus, animi id tempora rem!'

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("Make sure to provide atleast 1 tag", self.response_msg['Error'])
	

	def test_update_fail_empty_body(self):
		self.response_message = app.test_client().put('/questions/3',
			data = json.dumps({
		'title': 'Obviously theres quite some content on this title right',
		'posted_on': '13HRS AGO',
		'tags': ['Germany','Hitler','History','Fried Chicken','Krugler'],
		'answers': 34,
		'id': 8,
		'body': ''

		
		}),
			content_type= "application/json")
		self.response_msg = json.loads(self.response_message.data.decode("UTF-8"))
		self.assertEqual("You're message cannot be smaller than 20 characters", self.response_msg['Error'])


