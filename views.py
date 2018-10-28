import json
from flask import Response, request

from run import app, db
from response import not_found


@app.route('/')
def hello_world():
    return not_found('Hello, World!')
