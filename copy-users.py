import requests
import json
from collections import defaultdict
import sys

# copy all users from everyone.json to the mygroup

#curl -u admin:admin -FaddMembers=newuser http://localhost:4502/home/groups/N/NeuFUGsI1fmgLuUg3pFf.rw.html

pub1 = "http://localhost:4503"
mygroup = "/home/groups/a/mygroup"

everyone = []
with open('everyone.json') as f:
  master_json = json.load(f)
  everyone = master_json["members"]

for user in everyone:
	if ("/home/users" in user["home"]):
		name = user["id"]
		curlPostObj = {'addMembers': name}
		url = ''.join([pub1, mygroup, ".rw.html"])
		response = requests.post(url, data = curlPostObj, auth=("admin", "admin"))
		if (response.status_code != 200):
			print("".join(["Response ",response.text," for ",name]))
		else:
			print("".join(["Successfully added ",name]))