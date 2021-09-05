'''
Fill the code in endpoint from 59

json : plain string cross language, it could be convert a dict in python
'''

from flask import Flask, jsonify
# from flask.wrappers import Response


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
    return 'Hi'

@app.route('/store') 
def get_stores():
    print(type(jsonify({'stores':stores}))) # this will return a response
    return jsonify({'stores':stores}) # accept dict only

# POST /store data: {name:}
@app.route('/store',methods=['POST']) # only accept POST
def create_store():
    pass


# <> is the magic string, which gives parameters in your func
# http://127.0.0.1:5000/store/some_name
@app.route('/store/<string:name>') 
def get_store(name : str):
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/string:name/item',methods=['POST'])
def create_item_in_store(name : str):
    pass

@app.route('/store/string:name/item')
def get_item_in_store(name : str):
    pass


app.run(port=5000)