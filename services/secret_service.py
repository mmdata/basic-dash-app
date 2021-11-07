
import os

def secret_service():
	"""
	Read secrets from env variable and return them. 
	Always hash password when saving it to database.
	return ({os.environ['USERNAME']: os.environ['PASSWORD']})
	Here we just hard code the values: this is not production ready!
	"""
	return{
    'hello': 'world'
    }