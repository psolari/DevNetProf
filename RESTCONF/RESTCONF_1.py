import requests
from requests.auth import HTTPBasicAuth
import json

#global variables
base_url = "https://192.168.2.56/restconf/data/"
auth = ("psolari","psolari1")
headers = {
    "Accept":'application/yang-data+json',
    "Content-Type": "application/yang-data+json"
    }


# get_ospf_state
ospf_url = base_url + "Cisco-IOS-XE-ospf-oper:ospf-oper-data/ospf-state/ospf-instance=address-family-ipv4,16843009/ospf-area=0/ospf-interface=GigabitEthernet2/ospf-neighbor=192.168.2.55/state"
response = requests.get(ospf_url, headers=headers, auth=(auth), verify=False).json()
formatted_response = json.dumps(response, indent=4)
print(formatted_response)

#get_running_config
 native_url = base_url + "Cisco-IOS-XE-native:native/"
# response = requests.get(native_url, headers=headers, auth=auth, verify=False)
# if response.status_code == 200:
#     print("yes")
# formatted_response = json.dumps(response, indent=4)
# print(formatted_response)

#update_hostname
# payload = {"hostname": "R1"}
# hostname_url = native_url + "hostname/"
# response = requests.patch(hostname_url, headers=headers, auth=auth, verify=False, json=payload)
# if response.ok:
#     print(f'Hostname the device has been updated to {payload["hostname"]}')
# else:
#     print(response.status_code)

#add an interface
# payload = {
#     "Loopback": {
#         "name": 2,
#         "ip": {
#             "address": {
#                 "primary": {
#                     "address": "3.3.3.3",
#                     "mask": "255.255.255.255"
#                 }
#             }
#         }
#     }
# }
#
# interface_url = native_url + "interface/Loopback"
# response = requests.patch(interface_url, headers=headers, auth=auth, verify=False, json=payload)
#
# if response.ok:
#     print("Interface has been added")
#     print(response.text)
# else:
#     print(response.status_code)
#     print(response.text)

#add a static route
# payload = {
#     "Cisco-IOS-XE-native:ip-route-interface-forwarding-list": [
#         {
#                     "prefix": "3.3.3.3",
#                     "mask": "255.255.255.255",
#                     "fwd-list": [
#                         {
#                             "fwd": "192.168.2.55"
#                         }
#                     ]
#                 }
#             ]
#         }
#
#
# add_route_url = native_url + "ip/route/ip-route-interface-forwarding-list/"
# response = requests.post(add_route_url, headers=headers, auth=auth, verify=False, data=payload)
# if response.ok:
#     print("Route has been added")
#     print(response.text)
# else:
#     print(response.status_code)
#     print(response.text)
