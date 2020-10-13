import requests
import csv

author1 = "http://localhost:4502"
author2 = "http://otherhost:4502"
extension = ".infinity.json"

with open('page-paths.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		page_path = row[0]
		response1 = requests.get(author1 + page_path + extension, auth=('admin', 'admin'))
		response2 = requests.get(author2 + page_path + extension, auth=('admin', 'admin'))
		if (response1.text != response2.text): 
			print("Page mismatch: " + page_path + "\n")