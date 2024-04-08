from fabric import Connection
hosts= ["54.82.172.244", "100.27.14.106"]
for h in hosts:
    with Connection(
        host=h,
        user="ubuntu",
        connect_kwargs={
            "key_filename": "/home/deborah_rise/.ssh/id_rsa",
            },
        ) as c:
        c.local( )
