from ncclient import manager 
import xml.dom.minidom
USERNAME = 'cisco'
PASSWORD = 'cisco'
HOST = '192.168.0.202'
data = '''
      <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <statistics/>
        </interface>
      </interfaces-state>
      '''
with manager.connect(host=HOST, password=PASSWORD, port=830, username=USERNAME,hostkey_verify=False, device_params={'name':'iosxe'}) as m:
  c = m.get(filter=("subtree", data)).data_xml
  xml = xml.dom.minidom.parseString(c) 
  xml_pretty_str = xml.toprettyxml() 
  print(xml_pretty_str)