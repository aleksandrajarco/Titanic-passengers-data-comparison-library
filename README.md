# Titanic-passengers-data-comparison-library
#1. istall all dependencies
./run.sh

#2. setup search parmeters in parameters/<file>. You can store multiple files
#3. run python script:
python main.py [parameters]
  -h, --help       show this help message and exit
  --out OUT        path to the diff file
  --compare
  --diff
  --params PARAMS
  --localjson LOCALJSON


#example:

#compare local json identical to API search:
python main.py  --params parameters/params1  --compare --localjson files/file1.json

#compare local json different than API search:
python main.py  --params parameters/params1  --compare --localjson files/file2.json

#return diff of local json and API search to file:
python main.py --diff --out out/mydiff.json
