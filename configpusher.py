from nornir import InitNornir
from nornir.plugins.tasks.data import load_yaml
from nornir.plugins.tasks.text import template_file
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.functions.text import print_result

def load_data(task):
    data = task.run(
           task=load_yaml,
           file=f'{task.host["site"]}.yaml'
    )

    task.host["asn"] = data.result["asn"]
    task.host["networks"] = data.result["networks"]
    r = task.run(task=template_file, template="bgp.j2", path="")
    task.host["template_config"] = r.result
    task.run(task=netmiko_send_config, configuration=task.host["template_config"])



nr = InitNornir()

routers = nr.filter(platform='cisco_ios')
r = routers.run(load_data)
print_result(r)