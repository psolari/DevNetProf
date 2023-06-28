from ncclient import manager

# my_device = manager.connect(
#     host="192.168.2.38",
#     port="830",
#     timeout=30,
#     username="psolari",
#     password="jkm8DankFam!",
#     hostkey_verify=False
# )

devices = ["192.168.2.36","192.168.2.37"]

for device_ip in devices:
    with manager.connect(
        host=device_ip,
        port="830",
        timeout=30,
        username="psolari",
        password="jkm8DankFam!",
        hostkey_verify=False
    ) as m:
        for capability in m.server_capabilities:
            if "http://openconfig.net/yang/openconfig-ext?module=openconfig-extensions" in capability:
                print(capability)

