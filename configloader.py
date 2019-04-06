from nornir import InitNornir
from nornir.plugins.tasks.data import load_yaml
from nornir.plugins.functions.text import print_result
from nornir.core.inventory import ConnectionOptions

def load_data(task):
    data = task.run(
           task=load_yaml,
           file=f'{task.host["site"]}.yaml'
    )

    task.host["asn"] = data.result["asn"]
    task.host["networks"] = data.result["networks"]


nr = InitNornir()
nr.inventory.defaults.connection_options = ConnectionOptions(extras={"secret": "cisco"})
r = nr.run(task=load_data)
print_result(r)