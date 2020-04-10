import jsonparser as parser


def main(format, file_path, delimiter=None):
    formats = ["json", "csv"]
    assert (format in f for f in formats)
    file = open(file_path, "r")
    parsejson = parser.ParseJson(file)
    isjson = parsejson.isJson()
    parsejson.print_json()



main("json", "files/file2.json")
