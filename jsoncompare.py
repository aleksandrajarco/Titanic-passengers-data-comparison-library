class CompareJson():
    def __init__(self):
        pass

    def compare_one_to_one(self, json1, json2):

        if (type(json1) is dict and type(json2) is dict):

            # iterate over dictionary keys
            for dict_key, dict_value in json1.items():
                if(dict_key not in json2):
                    return False
                else:
                    #if dict_values are single values and  the same:
                    if (type(dict_value) is not dict and dict_value == json2[dict_key]):
                            return True
                    #if dict_value is dictionary type, compare two dicts
                    else:
                        if(self.compare_one_to_one(dict_value, json2[dict_key])):
                            return True
                        else:
                            return False

            return True

