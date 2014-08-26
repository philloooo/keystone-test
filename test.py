from flask import Flask
from keystoneclient.v2_0 import client
import json
from flask import request
import requests
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    print request.form
    if "auth_url" in request.form:        
    if "token" in request.form:
        try:
            client.Client(token=request.form['token'], auth_url)
    if all (k in request.form for k in ("username", "password","auth_url")):
        
        username=request.form['username']
        password=request.form['password']
        auth_url=request.form['auth_url']
        auth_data={"auth": {"identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "name":username,
                    "domain":{"id": "default"}, 
                    "password":password}}}}}
        headers= {'content-type': 'application/json'}
        r=requests.post(auth_url,data=json.dumps(auth_data),headers=headers)
        print r.text
        print r.json
        return "succeed"
    else:
        print 'need authorization'
        return 'need authorization' 

@app.route('/hello')
def hello():
    return "hello"

if __name__ == "__main__":
    app.debug = True    
    app.run(port=5001)
