from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_jokes import *

GOOGL_api = Blueprint('GOOGL_api', __name__,
                   url_prefix='/api/GOOGL')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(GOOGL_api)

class JokesAPI:
    # not implemented
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getJokes(GOOGL_data))

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getJoke(GOOGL_data, id))

    # getRandomJoke()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomJoke(GOOGL_data))
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countJokes(GOOGL_data)
            countMsg = {'count': count}
            return jsonify(countMsg)
        

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')

    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'http://stocks.nighthawkcodescrums.gq/' # run from web
    url = server + "/api/jokes"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
        ) 
    responses.append(
        requests.put(url+"/like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/jeer/"+num) # add to jeer count
        ) 

    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")