import requests
import json

# Global Variables
username = "vbrbfvpns8twx3j23axqctqw"
password = "bAJFURajcfEjMKpG7AHeBB23"

# Function to get Authorisation Token
def get_auth_token(user, pword):
    url = "https://id.cisco.com/oauth2/default/v1/token"
    payload = f'grant_type=client_credentials&client_id={user}&client_secret={pword}'
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
    response = requests.post(url, data=payload, headers=headers, verify=False)
    return response.json()

#Function to get EoX information by Product ID
def get_hardware_eox(token, models):
    header = {"Authorization": token, "Accept": "application/json"}
    eox_url = f'https://apix.cisco.com/supporttools/eox/rest/5/EOXByProductID/1/{models}'
    response = {}

    response = requests.get(eox_url, headers=header, verify=False)
    return response.json()


result = get_auth_token(username, password)
token = result["token_type"] + " " + result["access_token"]
#models = "ISR4451-X/K9,PWR-4450-AC,ACS-4450-FANASSY,ISR4451-X-4x1GE,GLC-LH-SMD,GLC-SX-MMD,CISCO3945-CHASSIS,C3900-SPE250/K9,PVDM3-256,TRPUG1ESXECISE2A0,PWR-3900-AC,Cisco Nexus 5672UP Switch,N9K-C9372PX-E,WS-C4948E,SFP-GE-S,PWR-C49E-300AC-R,C9500-48Y4C,C9500-48Y4,C9K-PWR-650WAC-R,C9K-T1-FANTRAY"
models = "5672UP"

#"SFP-10G-SR"
result = get_hardware_eox(token, models)
formatted_response = json.dumps(result, indent=4)
# for entry in result["EOXRecord"]:
#     print(entry["EOXInputValue"])
print(formatted_response)
