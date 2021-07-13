from lxml import html
import requests
import time

linkslistpage = "https://example.org/links.html"
basedomain = 'https://example.org'
dis1 = "https://dis1.example.org"
dis2 = "https://dis2.example.org"
dis3 = "https://dis3.example.org"

page = requests.get(linkslistpage)
tree = html.fromstring(page.content)
links = tree.xpath('//a/@href')
for page in links:
	# appending selector we want to caches
	sp_link = page.replace('.html','.sp.html')
	dis1_link = sp_link.replace(basedomain,dis1)
	dis1_response = requests.get(dis1_link)
	print('Cached: ', dis1_link)
	dis2_link = sp_link.replace(basedomain,dis2)
	dis2_response = requests.get(dis2_link)
	print('Cached: ', dis2_link)
	dis3_link = sp_link.replace(basedomain,dis3)
	dis3_response = requests.get(dis3_link)
	print('Cached: ', dis3_link)
	time.sleep(1)
