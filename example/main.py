import requests
from nexusdb import JSONDatabase
from datetime import datetime
import pytz
import json

ist = pytz.timezone('Asia/Kolkata')
utc_now = datetime.utcnow()
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ist)
ist_now_str = ist_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')

def users():
    payload = {
        "name": "name",
        "email": "email",
        "password": "password",
        "role": "admin"
    }
    return payload
    
users_data = users()
db = JSONDatabase('api')
db.create_collection('requests')
db.create_user(
    users_data['name'],
    users_data['email'],
    users_data['password'],
    users_data['role']
 )

url = 'http://api.vvfin.in/login'
protected_uri = "http://api.vvfin.in/protected"
data = {
    'email': users_data['email'],
    'password': users_data['password']
}
response = requests.post(url, json=data)
if response.status_code == 200:
    response_data = response.json()
    access_token = response_data.get('access_token')
    refresh_token = response_data.get('refresh_token')
    
    headers = {
    "Authorization": f"Bearer {access_token}"
    }
    
    protected_response = requests.get(protected_uri, headers=headers)
    
    if protected_response.status_code == 200: 
        data = protected_response.json()
        
        def protected_data():
            protected_uri_data = {
                "name": data['name'],
                "email": data['email'],
                "status": data['status']
            }
            return protected_uri_data
    else:
        print("Request failed with status code:", response.status_code, "error:", protected_response.json() )
        
    protected_data_json = protected_data()
    db.insert_document( 'requests', {
        "name": protected_data_json['name'],
        "email": protected_data_json['email'],
        "status": protected_data_json['status'],
        "access_token": access_token,
        "refresh_token": refresh_token,
        "timestamp": ist_now_str
    } )
else:
    print('Request failed with status code:', response.status_code, 'error: ', response.json())

