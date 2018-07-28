#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from test import db
from util import *

def do_targets(request):
	jsonDict = {"status":1}
	if request.method == 'GET':
		jsonDict = as_dict(db.get_targets())

	elif request.method == 'POST':
		id_added=db.add_target(request.json['name'])
		status = 0 if id_added == -1 else 1
		jsonDict = {
			"action":"add a target",
			"status":status,
			"id_added":id_added,
		}
	
	elif request.method == 'DELETE':
		id_array=request.json['ids']
		rows_rmed=0
		ids_result={}
		status=1
		for id in id_array:
			row_count = db.rm_target_byid(id)
			ids_result[str(id)]=row_count
			if row_count == -1:
				status = 0
			else:    
				rows_rmed += row_count
		jsonDict={
			"action":"delete targets",
			"status":status,
			"count_rmed":rows_rmed,
			"ids_rmed":ids_result,
		}
		
	return json.dumps(jsonDict,indent=4, sort_keys=True)

