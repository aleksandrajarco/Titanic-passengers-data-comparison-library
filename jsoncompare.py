class CompareJson():
    def __init__(self, json1, json2):
        self.json1 = json1
        self.json2 = json2

    def compare_one_to_one(self):
        x1 = list(self.json1.keys())
        x2 = list(self.json2.keys())

        if list(self.json1.keys()) == list(self.json2.keys()):
            return True
        else:
            return False


    def print_json1(self):
        print(list(self.json1.keys()))

    def print_json2(self):
        print(list(self.json2.keys()))
