from nornir import InitNornir
from nornir.plugins.tasks.data import load_yaml
from nornir.plugins.tasks.text import template_file
from nornir.plugins.tasks.networking import napalm_configure
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
    task.run(task=napalm_configure, configuration=task.host["template_config"])


#change variable names
nr = InitNornir()
routers = nr.filter(platform='ios')

r = routers.run(load_data)
print_result(r)