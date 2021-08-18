import json
import requests
from pprint import pprint
from postcode import PostCodeDict, PostCode

postcode_url = "https://api.postcodes.io/postcodes/"
postcode_request = requests.get(postcode_url + "WF6 2QT")

# print(postcode_request, type(postcode_request))
# print(postcode_request.content)
# pprint(postcode_request.json())
# pprint(type(postcode_request.json()))
#
# # Print latitude and longitude
#
# print("Latitude: ", postcode_request.json()['result']['latitude'])
# print("Longitude: ", postcode_request.json()['result']['longitude'])
#
pc = postcode_request.json()['result']
#
# print("Latitude: ", pc['latitude'])
# print("Longitude: ", pc['longitude'])


postcodes = {'postcodes': ["WF6 2QT", "WF1 2NB", "WF1 4JZ"]}
body = json.dumps(postcodes)
headers = {'Content-Type': 'application/json'}

multi_pc_req = requests.post(postcode_url, headers=headers, data=body)
# pprint(multi_pc_req)

multi_pc = multi_pc_req.json()['result']
# print(multi_pc['WF6 2QT']['result'])


# for postcode in multi_pc:
#     result = postcode['result']
#     print(f"""
#     Postcode: {result['postcode']}
#     Latitude: {result['latitude']}
#     Longitude: {result['longitude']}
# """)

for postcode in multi_pc:
    result = PostCodeDict(postcode['result'])
    print(f"""
    Postcode: {result['postcode']}
    Latitude: {result['latitude']}
    Longitude: {result['longitude']}
""")
#
#
# pcc = PostCode('WF6 2QT')
#
# print(pcc.latlong())
# print(pcc.easnor())

