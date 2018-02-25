import random
import json

class RandAmazon
	#constructor
	#reads filename as JSON file and stores it as a dictionary in dictData and stores the size of dictionary in size
	def __init__(self, filename):
		self.dictData = json.load(open(filename))
		self.size = datastore["size"]

	#generates a random numer within the size of the dictionary and returns item as dictionary
	#returned dictionary contains "title", "image", and "price"
	def generateRand():
		return self.dictData[str(random.randint(1,size))]