from ncclient import manager

my_device = manager.connect(
    host="192.168.2.38",
    port="830",
    timeout=30,
    username="psolari",
    password="jkm8DankFam!",
    hostkey_verify=False
)

for capability in my_device.server_capabilities:
    print(capability)

my_device.close_session()
