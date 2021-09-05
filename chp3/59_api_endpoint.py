'''
Create resful endpoints without functionality
'''

from flask import Flask


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

# POST /store data: {name:}
@app.route('/store',methods=['POST']) # only accept POST
def create_store():
    pass


# <> is the magic string, which gives parameters in your func
# http://127.0.0.1:5000/store/some_name
@app.route('store/<string:name>') 
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