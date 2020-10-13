import requests
import csv
import json
from collections import defaultdict
import sys

# script to run queries in a set of directories, 
# looking for usages of a specific list of assets
​
author = "http://localhost:4502/"
querypart1 = "bin/querybuilder.json?type=nt:unstructured&path=/content/proj"
querypart2 = "&1_property=fileReference&1_property.value="
querypart3 = "&orderby=path"
​
paths = []
with open("content-nodes-list.csv") as nodes_csv_file:
    nodes_csv_reader = csv.reader(nodes_csv_file, delimiter=",")
    for node_row in nodes_csv_reader:
        paths.append(node_row[0])
check_paths = tuple(paths)
​
print("path,asset,lastModified")
​
with open("assets-list.csv") as assets_csv_file:
    assets_csv_reader = csv.reader(assets_csv_file, delimiter=",")
    for row in assets_csv_reader:
        asset_name = row[0]
        request_path = f"{author}{querypart1}{querypart2}{asset_name}{querypart3}"
        response = requests.get(request_path, auth=("admin", "admin"))
        jsonResponse = response.json()
        pagehits = jsonResponse["hits"]
        print(f"Found {len(pagehits)} for {asset_name}", flush=True, file=sys.stderr)
        for _ in pagehits:
            hit = defaultdict(lambda: "")
            # print(_, file=sys.stderr)
            for k, v in _.items():
                hit[k] = v
            if hit["path"].startswith(check_paths):
                print(f"{hit['path']},{asset_name},{hit['lastModified']}", flush=True)