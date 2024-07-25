# import the python request library
import json

import requests

# auth token variable initialization
auth_token = "d0357de610615423c1285cf189e84657cedf9d50"

# parameters dictionary declaration and initialisation
par = {"name": "Sithabile Chikowero", "groups": [], "urns": ["tel:+263 7875408292"]}

# headers variable declaration and initialisation
headers = {'Content-Type': 'application/json', 'Authorization': 'Token ' + auth_token}

# post method call with relevant arguments and variable initialization
req = requests.post("https://2waychat.com/api/v2/contacts.json", data=json.dumps(par), headers=headers)

# print the response from the post request
print(req.text)