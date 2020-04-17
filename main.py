import jsonparser as parser
from jsoncompare import CompareJson
import requests
import html
import json
import sys

import argparse

argparser = argparse.ArgumentParser(description='')
argparser.add_argument('--out', type = str, action= 'store', help='path to the diff file')
argparser.add_argument('--compare', action="store_true", default=False)
argparser.add_argument('--diff', action="store_true", default=False)
argparser.add_argument('--params', action="store", default = "parameters/params1")
argparser.add_argument('--localjson', action="store", default = "files/file1.json")


def read_params_from_file(path):
    params = open(path,"r")
    params_dict = {}
    for line in params.readlines():
        key, value = line.split(":")[0].strip(), line.split(":")[1].strip()
        params_dict[key]=value
    return params_dict

def readFromAPI(endpoint,survived, age, pclass,  timezone, rows, records ):
    #url="https://public.opendatasoft.com/api/records/1.0/search/?dataset=titanic-passengers&rows=1&facet=survived&facet=pclass&facet=sex&facet=age&facet=embarked&refine.survived=Yes&refine.pclass=2&refine.age=23.0&timezone=Europe%2FBerlin"

    url = '{}/records/{}/search/?dataset=titanic-passengers&rows={}&facet=survived&facet=sex&facet=age&facet=embarked&refine.survived={}&refine.pclass={}&age={}%timezone={}'.format(endpoint,records,rows,survived,pclass,age,escape_html(timezone))
    url= url.replace(" ", "")
    #print(url)
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



def main( ):
    args = argparser.parse_args()
    out = args.out
    param =args.params
    localjson = args.localjson
    # print(parser.parse_args(['-out']))

    if (args.compare == True or args.diff == True) :
        compare = CompareJson()

        params_dict = read_params_from_file(param)

        file = open(localjson, "r")
        data = file.read()
        parse = parser.ParseJson(data)

        parse.string_to_json()
        json1 = parse.json_object

        endpoint = "https://public.opendatasoft.com/api "
        json2 = readFromAPI(endpoint, params_dict['survived'], params_dict['age'], params_dict['pclass'],
                            params_dict['timezone'], params_dict['rows'], params_dict['records'])
        # json2 = readFromAPI(endpoint, "Yes", 23, 2, 'Europe/Berlin', 1, 1.0)

        parse2 = parser.ParseJson(json2)

        parse2.dict_to_json()
        json2 = parse2.json_object
        if(args.compare == True):


            # print("dict object={}".format(type(parse2.json_object)))

            result = compare.compare_one_to_one(json1, json2)
            print(result)

        if(args.diff==True):

            compare.print_json_diff_to_file(out, json1, json2)







    #p =argparser.parse_args('out')


#params_dict = read_params_from_file("parameters/params1")
main()
