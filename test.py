from flask import Flask
from keystoneclient.v2_0 import client
from flask import request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def auth():
    print request.form
    if "auth_url" in request.form:        
        auth_url=request.form['auth_url']
        if "token" in request.form:
            try:
                client.Client(token=request.form['token'], auth_url)
                return 'succeed'
            except: 
                return "error authentication"
        elif all (k in request.form for k in ("username", "password","tenant_name")):
            username=request.form['username']
            password=request.form['password']
            tenant_name=request.form['tenant_name']
            try:
                client.Client(username=username, password=password,tenant_name=tenant_name,
                    auth_url)
                return "succeed"
            except:
                return "error authorization"
    return 'need authorization' 


if __name__ == "__main__":
    app.debug = True    
    app.run(port=5001)
