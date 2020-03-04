import requests
import json
 
url="https://api.betfair.com/exchange/betting/json-rpc/v1"
header = { 'X-Application' : 'lwWV5oRFKzm3fnn8', 'X-Authentication' : 'e0ozo8IZTzUcNZ18XsyEq2+0Yxh2BiXcIs/a6bCweP8=' ,'content-type' : 'application/json' }
 
jsonrpc_req='{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEvents", "params": {"filter": {"eventTypeIds": ["7"]}}, "id": 1}'
 
response = requests.post(url, data=jsonrpc_req, headers=header)
 
print(json.dumps(json.loads(response.text), indent=3))

print("JAK TI JEBEEEEEEEEEEE JAK TI JEBE")

jsonrpc_req='{"jsonrpc": "2.0", "method": "ScoresAPING/v1.0/listRaceDetails", "params": {"filter":{ }}, "id": 1}'
  
response = requests.post(url, data=jsonrpc_req, headers=header)
  
print(json.dumps(json.loads(response.text), indent=3))