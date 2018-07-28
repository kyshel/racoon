#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import json
import sys


def raw_response(targetURL):
	response = requests.get(targetURL)
	a=json.dumps(dict(response.headers),indent=4, sort_keys=True)
	return a


def parse_post_data(data):
	if data['op'] == 'getUrlsStatusCode':
		return get_urls_status_code(data['urls'])
	elif data['op'] == 'getUrlStatusCode':
		return get_url_status_code(data['url'])


def get_urls_status_code(urls_list):
	urls_with_status_code=[]
	for x in urls_list:
		line = [[x,get_url_status_code(x)]]
		urls_with_status_code+=line
	return urls_with_status_code


def get_url_status_code(targetURL):
	TIME_OUT_CONNECTION = 2
	TIME_OUT_READ = 3
	statusCode = None
	try:
		response = requests.head(targetURL, timeout=(TIME_OUT_CONNECTION, TIME_OUT_READ))
	except Exception as e:
		statusCode=600       
	else:
		statusCode=response.status_code
	finally:
		return statusCode




# raw_response("http://nixni.cc")












# r = {'is_claimed': 'True', 'rating': 3.5}
# r = json.dumps(r)
# loaded_r = json.loads(r)
# loaded_r['rating'] #Output 3.5
# type(r) #Output str
# type(loaded_r) #Output dict