from nornir.core.inventory import ConnectionOptions

def adapt_host_data(host):

    # This function receives a Host object for manipulation
    host.username = host["user"]
    host.password = host["password"]
    host.connection_options["napalm"] = ConnectionOptions(
        extras={
            "optional_args": {
                "secret":host.password
            }
        }
    )
