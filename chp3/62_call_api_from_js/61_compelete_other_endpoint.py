'''
Fill the code in endpoint from 59

request is different from requests(another python package)
'''

from flask import Flask, jsonify, request, render_template

# 


app = Flask(__name__) # unique name of this file as app name

stores = [
    {
    'name' : 'My Wonderful Store',
    'items':[
        {
            "name" : "My Item",
            'price' : 15.99
        }
    ]
    }
]

# POST - used to receive data
# GET - used to send data back only

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store') 
def get_stores():
    # print(type(jsonify({'stores':stores}))) # this will return a response
    return jsonify({'stores':stores}) # accept dict only

# POST /store data: {name:}
# return the post data which means add data successfully
@app.route('/store',methods=['POST']) # only accept POST
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'item' : []
    }
    stores.append(new_store)
    return jsonify(new_store)


# <> is the magic string, which gives parameters in your func
# http://127.0.0.1:5000/store/some_name
@app.route('/store/<string:name>') 
def get_store(name : str):
    for s in stores:
        if s['name'] == name:
            return jsonify(s)
    return jsonify({'message' : "store not found"})



# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name : str):
    request_data = request.get_json()
    for s in stores:
        if s['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message' : 'store not found'})


@app.route('/store/<string:name>/item')
def get_item_in_store(name : str):
    print(stores)
    for s in stores:
        if s['name'] ==name:
            return jsonify({'items':s['items']})
    return jsonify({'message' : 'store not found'})


app.run(port=5000)