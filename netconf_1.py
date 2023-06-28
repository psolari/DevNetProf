from ncclient import manager
import xml.dom.minidom
from rich import print as rprint

# my_device = manager.connect(
#     host="192.168.2.38",
#     port="830",
#     timeout=30,
#     username="psolari",
#     password="jkm8DankFam!",
#     hostkey_verify=False
# )

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
            if "http://openconfig.net/yang/openconfig-ext?module=openconfig-extensions" in capability:
                filter_template  = f"""
                <native xmlns ="{capability}">
                </native>
                """
                my_filter = filter_template.format(capability=capability)
                results = m.get(filter=('subtree', my_filter))
                pretty_results = xml.dom.minidom.parseString(str(results)).toprettyxml()
                rprint(pretty_results)


for device_ip in devices:
    get_device_config(device_ip)
