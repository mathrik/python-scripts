import requests
import csv

author = "http://localhost:4502/"
extension = ".json"

with open('bad-replication-status.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		page_path = row[0]
		response = requests.get(author + page_path + extension, auth=('admin', 'admin'))

		responseText = response.text
		strFound = responseText.find("cq:lastReplicationAction\":\"Activate")
		if (strFound < 0): 
			print("Page not activated: " + page_path + "\n")
