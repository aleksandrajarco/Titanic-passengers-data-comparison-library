import unittest
import jsoncompare as compare
from jsoncompare import CompareJson

class TestJsonCompare(unittest.TestCase):

    # Returns True or False.
    def test_compare_one_to_one(self):

        json1 = {"k1":{"k3":"v3"}, "k2":"v2"}
        json2 = {"k2":"v2", "k1":{"k3":"v3"}}
        compare=CompareJson()
        result = compare.compare_one_to_one(json1, json2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
