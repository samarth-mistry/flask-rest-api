from flask import Flask, jsonify

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
    return "LANDING!"

@app.route('/store',methods=['POST'])
def createStore():
    pass

@app.route('/store/<string:name>')
def getStore(name):
    pass

@app.route('/store')
def getStores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def createItemInStore(name):
    pass

@app.route('/store/<string:name>/item')
def getItemsInStore(name):
    pass

app.run(port=5000)