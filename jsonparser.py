import json
import csv

class ParseJson():
    def __init__(self, data):
        #self.file = file
        #self.__dict__ = json.loads(data)
        #self. fileType = None
        self.data = data
        self.json_object = None
        #self.is_json()

    def dict_to_json(self):
        self.json_object= json.dumps(self.data)
        self.json_object = json.loads(self.json_object)

    def string_to_json(self):
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
        print("json object:{}".format(self.json_object))

    def sort_json(self):
        self.json_object = json.dumps(self.json_object, indent=4, sort_keys=True)




