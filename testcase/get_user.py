import requests
import json
from login import test_Login as login

def test_get_user():
    # headers.
    headers = {'Authorization': login()["token"]}
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.get(login()["urlBase"] +'/api/users/2',headers=headers)
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    #respJson = json.loads(resp.text)

    

