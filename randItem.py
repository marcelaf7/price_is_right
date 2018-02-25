import random
import json

datastore = json.load(open('AmazonData.JSON'))

size = datastore["size"]

randDict = datastore[str(random.randint(1,size))]