import requests
import json
from requests.auth import HTTPBasicAuth

dnac_ip = "10.10.20.85"

token = requests.post('https://10.10.20.85/dna/system/api/v1/auth/token',auth=HTTPBasicAuth(username='administrator',password='Cisco1234!'),
headers={'content-type': 'application/json'},verify=False,)
data = token.json()

print(data["Token"])

token = data["Token"]

response = requests.get('https://{}/dna/intent/api/v1/network-device'.format(dnac_ip),
headers={'X-Auth-Token': token,'Content-type': 'application/json'},verify=False)

print("#################Response from Catalyst Center############################")    
print(json.dumps(response.json(), indent=4))

#/api/vl/network-device?softwareType=I0S-XE&softwareVersion=16.4.2
#'https://{}/dna/intent/api/v1/network-device?softwareType=IOS-XE&hostname=sw2'
#'https://{}/dna/intent/api/v1/network-device'