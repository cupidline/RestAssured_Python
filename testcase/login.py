import requests
import json

def test_Login():
    urlBase = 'https://reqres.in'
    
    # headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.post(urlBase +'/api/login', data = json.dumps(payload,indent=4),headers=headers)
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    respJson = json.loads(resp.text)
    token = "Bearer " + respJson["token"]
    print(token)
    return ({"urlBase":urlBase,"token":token})
    

