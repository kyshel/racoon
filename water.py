#!/usr/bin/env python
from flask import Flask, send_from_directory, request, url_for
from pprint import pprint
import json
import sys


from test import db
import r_ant # del
import core

app = Flask(__name__)

@app.route('/')
def index():
    return send_static('index.html')   

@app.route('/api/targets', methods=['GET','POST','DELETE'])
def targets():
    return core.do_targets(request)
    



















@app.route('/api2', methods=['POST', 'GET'])
def api2():
    if request.method == 'POST':
        result=r_ant.parse_post_data(request.json);
        return json.dumps(result,indent=4, sort_keys=True)
    else:
        jsonStr=r_ant.raw_response("https://github.com")
        return jsonStr








###############################################################################


# list all api
def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route("/api")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return json.dumps(links,indent=4, sort_keys=True)

# static 
@app.route('/<path:filename>')
def send_static(filename):
    return send_from_directory('static',
                               filename)

if __name__ == '__main__':
    app.run(debug=True)