from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.00
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

#POST   /store data: {name:}
@app.route('/store', methods=['POST'])
def createStore():
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)


#GET    /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def getStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(stores)
    return jsonify({'message': f"store {name} was not found."})


#GET    /store
@app.route('/store', methods=['GET'])
def getStores():
    return jsonify({'stores': stores})


#POST   /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
        if store['name'] == name:
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['items'].append(newItem)
            return jsonify(newItem)
    return jsonify({'message': f"store {name} was not found."})


#GET    /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def getItemsInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': f"store {name} was not found."})


app.run(port=5000)