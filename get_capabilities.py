from ncclient import manager

devices = ["192.168.2.36","192.168.2.37"]


def get_device_config(device_ip):
    with manager.connect(
        host=device_ip,
        port="830",
        timeout=30,
        username="psolari",
        password="jkm8DankFam!",
        hostkey_verify=False
    ) as m:
        for capability in m.server_capabilities:
            print(capability)

for device_ip in devices:
    get_device_config(device_ip)
