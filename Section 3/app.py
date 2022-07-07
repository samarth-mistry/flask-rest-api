from flask import Flask, jsonify, request, render_template

app=Flask(__name__)

stores = [
    {
        "name": "DD Store",
        "items": [
            {
                "name": "Item 1",
                "price": 16.99
            }
        ]
    },
    {
        "name": "City Sq. Mart",
        "items": [
            {
                "name": "Item 2",
                "price": 993.99
            }
        ]
    }
]

@app.route('/')
def landing():
    return render_template('index.html')
    # return "LANDING!"

@app.route('/store',methods=['POST'])
def createStore():
    req_data = request.get_json()
    new_store = {
        'name': req_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def getStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({ 'message': 'No reult found!' })

@app.route('/store')
def getStores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def createItemInStore(name):
    req_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": req_data['name'],
                'price': req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    
    return jsonify({ 'message': 'No reult found!' })

@app.route('/store/<string:name>/item')
def getItemsInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({ 'message': 'No reult found!' })



app.run(port=5000)