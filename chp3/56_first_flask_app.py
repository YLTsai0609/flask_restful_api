'''
Flask : the server read client request
'''

from flask import Flask


app = Flask(__name__) # unique name of this file as app name

@app.route('/') # like htpp://www.google.com/
def home():
    return "Hello world"

app.run(port=5000)