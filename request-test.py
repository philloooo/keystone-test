import requests
data={"username":"phi", "password":"phi", "tenant_name":"admin","auth_url":"http://127.0.0.1:5000/v2.0"}
r=requests.post("http://127.0.0.1:5001",data=data)
print r.text

