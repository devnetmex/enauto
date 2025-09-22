import requests
import sys
requests.packages.urllib3.disable_warnings()
HOST = '192.168.0.202'
PORT = 443
USER = 'cisco'
PASS = 'cisco'
def main():
 url = "https://{h}:{p}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(h=HOST, p=PORT)
 headers = {'Content-Type':	'application/yang-data+xml','Accept':	'application/yang-data+xml'}
 response = requests.get(url, auth=(USER,PASS),headers=headers, verify=False)
 print(response.text)
if  __name__  == '__main__' :
 sys.exit(main())