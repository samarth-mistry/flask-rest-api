from flask import Flask, request
from collections import Mapping
from flask_restful import Resource, Api
from flask_jwt import JWT

app = Flask(__name__)
app.secret_key = '08-07-2022'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        #item = list(filter(lambda x: x['name' == name, items]))
        item = next(filter(lambda x: x['name' == name, items]), None) #first item

        return {'item': item}, 200 if item else 404
        #return {'message': 'No match found!'}

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "Item '{}' already exists.".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

        #202 accepted
        #200 ok

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)