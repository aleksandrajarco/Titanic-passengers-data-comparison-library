import jsonparser as parser
from jsoncompare import CompareJson
import requests
import html
import json


def readFromAPI(endpoint,survived, age, pclass,  timezone, rows, records ):
    #url="https://public.opendatasoft.com/api/records/1.0/search/?dataset=titanic-passengers&rows=1&facet=survived&facet=pclass&facet=sex&facet=age&facet=embarked&refine.survived=Yes&refine.pclass=2&refine.age=23.0&timezone=Europe%2FBerlin"

    url = '{}/records/{}/search/?dataset=titanic-passengers&rows={}&facet=survived&facet=sex&facet=age&facet=embarked&refine.survived={}&refine.pclass={}&age={}%timezone={}'.format(endpoint,records,rows,survived,pclass,age,escape_html(timezone))
    url= url.replace(" ", "")
    #url = "https://public.opendatasoft.com/explore/dataset/titanic-passengers/api/?timezone=Europe%2FBerlin&rows=1&refine.survived=Yes&refine.pclass=2&refine.age=23.0"
    #print(url)
    response = requests.get(url)
    #print(response)
    #print(response.text)
    #print(type(response.json))
    return response.json()

def escape_html(text):
    """escape strings for display in HTML"""
    return html.escape(text, quote= True).\
        replace(u'/', u'%2F')

def main(format, file_path, delimiter=None):
    formats = ["json", "csv"]
    assert (format in f for f in formats)
    file = open(file_path, "r")
    data = file.read()
    parse = parser.ParseJson(data)

    parse.string_to_json()
    json1 = parse.json_object

    endpoint = "https://public.opendatasoft.com/api "
    json2 = readFromAPI(endpoint, "Yes", 23, 2, 'Europe/Berlin', 1, 1.0)
    #print(type(json2))
    parse2 = parser.ParseJson(json2)

    parse2.dict_to_json()
    json2 = parse2.json_object
    #print("dict object={}".format(type(parse2.json_object)))

    compare = CompareJson()

    result = compare.compare_one_to_one(json1, json2)
    print(result)




main("json", "files/file2.json")
