import unittest
import jsonparser as parser
from jsoncompare import CompareJson

class TestJsonParser(unittest.TestCase):

    #def __init__(self):
    #    self.json_string="{'key1': 'value1', 'key2': 'value2'}"
    #    self.json_dict = {'key1': 'value1', 'key2' : 'value2'}
    #    self.parse_string = parser.ParseJson(self.json_string)
    #    self.parse_dict = parser.ParseJson(self.json_dict)


    # Returns True or False.
    def test_dict_to_json(self):
        #self.parse_string
        #print(self.parse_dict)
        json_dict = {"key1": "value1", "key2": "value2"}
        parse_dict = parser.ParseJson(json_dict)
        parse_dict.dict_to_json()
        self.assertTrue(parse_dict.json_object["key1"] == "value1")

    def test_string_to_json(self):
        json_string= '{"key1": "value1", "key2": "value2"}'
        parse_string = parser.ParseJson(json_string)
        parse_string.string_to_json()
        self.assertTrue(parse_string.json_object["key1"] == "value1")


if __name__ == '__main__':
    unittest.main()
