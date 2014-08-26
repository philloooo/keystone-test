import requests
data={"username":"phi", "password":"phi", "auth_url":"http://127.0.0.1:5000/v3/auth/tokens"}
r=requests.post("http://127.0.0.1:5001",data=data)
print r.text

