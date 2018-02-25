import random
import json


class RandAmazon:


    # constructor
    # reads filename as JSON file and stores it as a dictionary in dictData and stores the size of dictionary in size
    def __init__(self, filename):
        self.dictData = json.load(open(filename))
        self.size = self.dictData["size"]
        self.history = []

    # generates a random number within the size of the dictionary and returns item as dictionary
    # returned dictionary contains "title", "image", and "price"
    def generateRand(self):
        randnum = random.randint(0, self.size - 1)
        if len(self.history) == self.size:
            self.history = []

        if randnum in self.history:
            for x in range(len(self.history)):
                if x not in self.history:
                    randnum = x
                    break

        self.history.append(randnum)

        print(randnum)

        return self.dictData[str(randnum)]