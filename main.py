from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from tally_webhook import new_response

app = Flask('')
api = Api(app)


class home(Resource):

  def get(self):
    return jsonify({'Hello': 'world!'})


class tally_new_response(Resource):

  def post(self):
    data = json.loads(request.get_data().decode('latin1'))
    # print(data)
    new_response(data)
    # return final_response


api.add_resource(home, '/')
api.add_resource(tally_new_response, '/api/tally/newresponse')

app.run(host='0.0.0.0', port=6000, debug=True)
