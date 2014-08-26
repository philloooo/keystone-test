from flask import Flask
from keystoneclient.v2_0 import client
from flask import request
app=Flask(__name__)

def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print request.form
        if "auth_url" in request.form:        
            auth_url=request.form['auth_url']
            if "token" in request.form:
                try:
                    client.Client(token=request.form['token'], auth_url)
                    return f(*args, **kwargs)
                except: 
                    return "error authentication"
            elif all (k in request.form for k in ("username", "password")):
                username=request.form['username']
                password=request.form['password']
                try:
                    if "tenant_name" in request.form:
                        tenant_name=request.form['tenant_name']
                        client.Client(username=username, password=password,tenant_name=tenant_name,
                            auth_url)
                    elif "tenant_id" in request.form:
                        tenant_id=request.form['tenant_id']
                        client.Client(username=username, password=password,tenant_id=tenant_id,
                        auth_url)
                    else:
                        client.Client(username=username, password=password,auth_url)
                    return f(*args, **kwargs)

                except:
                    return "error authorization"
    return decorated_function

@app.route('/',methods=['GET','POST'])
@auth
def login():
    return "true"

if __name__ == "__main__":
    app.debug = True    
    app.run(port=5001)
