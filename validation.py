class PostValidator():
	"""docstring for PostValidator"""
	

	def validateBody(self, body):
		""" This function validates the question body"""
		if body['body'] != '' and len(body['body']) > 20:
			return body
		else:
			return({"Error":"You're message cannot be smaller than 20 characters"})


	def validateID(self,body):
		""" This function validate the question id """
		if body['id'] != 0 and body['id'] != '':
			return body
		else:
			return({"Error":"Question id cannot be zero"})


	def validateTags(self,body):
		""" This function validate the tags """
		if len(body['tags']) != 0:
			return body
		else:
			return({"Error":"Make sure to provide atleast 1 tag"})



	def validateTitle(self,body):
		""" This function validates the title """
		if body['title'] != '' and len(body['title']) > 14:
			return body
		else:
			return({"Error": "Please ensure that  your title is larger than 14 characters"})
		
		