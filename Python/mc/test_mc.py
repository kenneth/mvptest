import pylibmc
mc = pylibmc.Client(["127.0.0.1"], binary=True,behaviors={"tcp_nodelay": True,"ketama": True})
mc["some_key"] = "Some value"
print mc["some_key"]