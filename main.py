import feedparser
import sys
import json
from pprint import pprint
import time
import requests
import urllib3

def get_feed_urls(filename):
	urls=[]
	fp = open(filename)
	feeds = fp.readlines()
	for feed in feeds:
		feedobj = feedparser.parse(feed)
		entries=[]
		entries.extend(feedobj['items'])
		print(len(entries))
		for entry in entries:
			urls.append(entry['links'][0]['href'])
	return urls

def get_random_user_agent():
	return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def make_random_http_requests(urls):
	for URL in urls:
		print(URL,end=" -->")
		http = urllib3.PoolManager()
		try:
			response = http.request('GET',URL,timeout=4.0)
			#response = requests.get(url, headers=get_random_user_agent())
			print(response.status)
		except Exception:
			pass
		time.sleep(2)

def main():
	urls = get_feed_urls(sys.argv[1])
	make_random_http_requests(urls)

if __name__ == '__main__':
	main()