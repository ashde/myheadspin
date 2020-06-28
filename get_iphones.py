#!/usr/bin/env python

import headspin.db as db
import headspin.model.device_note_model as dm
import headspin.model.pool_model as pm

def run(host):
    import subprocess
    with open('/dev/null', 'w') as devnull:
        # print(host + " ++ DEUBG ++ " )
        out = subprocess.check_output(['ssh', '-F', '/Users/ash/headspinio/keys-red/dev/ssh-config', '-o', 'BatchMode=yes', '-o', 'UserKnownHostsFile=/dev/null', '-o', 'StrictHostKeyChecking=no', host, `idevice_id -l`], stderr=devnull)
        print("{} = {}".format(host, out.strip()))

def main():
    hosts = """
        proxy-au-lil-2-i.headspin.io
        proxy-au-hlt-2-i.headspin.io
        proxy-au-bri-2-i.headspin.io
        proxy-au-ade-3-i.headspin.io
        proxy-au-pal-2-i.headspin.io
        proxy-cn-shg-0-i.headspin.io
        proxy-mx-mex-8-i.headspin.io

    """
    # print(hosts)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as pool:
        for host in hosts.split():
            pool.submit(run, host)

main()
