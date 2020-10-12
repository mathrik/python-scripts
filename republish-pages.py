import requests
import csv
import json
from collections import defaultdict
import sys
import datetime
from dateutil.parser import parse

pub1 = "http://localhost:4503"
extension = "/_jcr_content.2.json"
activateUrl = "http://localhost:4502/bin/replicate.json"
passWd = "admin$1st3r"

paths = []
with open("list-of-paths.csv") as nodes_csv_file:
    nodes_csv_reader = csv.reader(nodes_csv_file, delimiter=",")
    for node_row in nodes_csv_reader:
        paths.append(node_row[0])
check_paths = tuple(paths)

goodDateTimeObj = parse("Oct 5 2020 00:00:00  GMT-0700")

for path in paths:
	request_path = "".join([pub1,path,extension])
	#print(request_path)
	response = requests.get(request_path, auth=("admin", passWd))
	if (response.status_code != 404):
		jsonResponse = response.json()
		lastModified = jsonResponse["cq:lastModified"]
		lastModifiedObj = parse(lastModified)
		if (lastModifiedObj > goodDateTimeObj):
			print("".join([path," is in the clear"]))
		else:
			curlPostObj = {'path': path, 'cmd': 'activate'}
			publishResponse = requests.post(activateUrl, data = curlPostObj, auth=("admin", passWd))
			print("".join(["Activating ",path,": ",str(publishResponse.status_code)]))
	else:
		curlPostObj = {'path': path, 'cmd': 'activate'}
		publishResponse = requests.post(activateUrl, data = curlPostObj, auth=("admin", passWd))
		print("".join(["Activating ",path,": ",str(publishResponse.status_code)]))