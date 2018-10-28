import json
from flask import Response

def json_response(response, status):
    return Response(json.dumps(response, indent=4, sort_keys=True), status=status, mimetype="application/json") 

def success(response):
    return json_response(response, 200)

def not_found(response):
    return json_response(response, 404)

def permission_denied(response):
    return json_response(response, 403)

def created(response):
    return json_response(response, 201)

def accepted(response):
    return json_response(response, 202)

def bad_request(response):
    return json_response(response, 400)

def server_error(response):
    return json_response(response, 500)