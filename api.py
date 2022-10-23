from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 

from model_data import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/data')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class StocksAPI:
    # get stocks()
    class _Read(Resource):
        def get(self):
            return jsonify(getStocks())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getStocks(id))


    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    
if __name__ == "__main__": 
    server = "http://127.0.0.1:5000/" # run local
    # server = 'https://unblockstuff.duckdns.org/' # run from web
    url = server + "/api/data"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']
    
    # Cycle through and print responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("data error")