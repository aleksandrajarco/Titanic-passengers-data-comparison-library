import json
import csv

class ParseJson():
    def __init__(self, file):
        self.file = file
        #self.__dict__ = json.loads(data)
        self. fileType = None
        self.data = file.read()
        self.json_object = None
        self.isJson()

    def isJson(self):
        try:
            #print(self.data)
            self.json_object = json.loads(self.data)
            return True
        except:
            return False

        #print(json_object)
        if (self.json_object):
            self.fileType = "json"

    def print_json(self):
        print(self.json_object)



