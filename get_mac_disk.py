#!/usr/bin/env python

import headspin.db as db
import headspin.model.device_note_model as dm
import headspin.model.pool_model as pm

def run(host):
    import subprocess
    with open('/dev/null', 'w') as devnull:
        # print(host + " ++ DEUBG ++ " )
        out = subprocess.check_output(['ssh', '-F', '/Users/ash/headspinio/keys-red/dev/ssh-config', '-o', 'BatchMode=yes', '-o', 'UserKnownHostsFile=/dev/null', '-o', 'StrictHostKeyChecking=no', host, 'diskutil info disk0 | grep "Media Name"'], stderr=devnull)
        print("{} = {}".format(host, out.strip()))

def main():
    hosts = """
dev-au-bri-1-proxy-2-i.headspin.io
dev-au-dev-0-proxy-2-i.headspin.io
dev-au-ltb-0-proxy-3-i.headspin.io
dev-au-mel-1-proxy-1-i.headspin.io
dev-au-ool-0-proxy-2-i.headspin.io
dev-au-ool-1-proxy-2-i.headspin.io
dev-au-ool-2-proxy-2-i.headspin.io
dev-au-ool-3-proxy-2-i.headspin.io
dev-au-qps-0-proxy-0-i.headspin.io
dev-au-syd-0-proxy-6-mac-i.headspin.io
dev-au-syd-1-proxy-1-i.headspin.io
dev-br-sao-0-proxy-0-mac-i.headspin.io
dev-br-sao-0-proxy-14-mac-i.headspin.io
dev-br-sao-2-proxy-0-mac-i.headspin.io
dev-br-sao-2-proxy-3-mac-i.headspin.io
dev-cl-scl-0-proxy-0-i.headspin.io
dev-cn-bej-0-proxy-0-i.headspin.io
dev-cn-gua-0-proxy-0-i.headspin.io
dev-cn-shg-0-proxy-5-mac-i.headspin.io
dev-de-dus-1-proxy-0-i.headspin.io
dev-fr-par-0-proxy-12-mac-i.headspin.io
dev-gb-lhr-0-proxy-16-mac-i.headspin.io
dev-gb-lhr-0-proxy-19-mac-i.headspin.io
dev-gh-acc-2-proxy-2-mac-i.headspin.io
dev-hk-hkg-0-proxy-8-mac-i.headspin.io
dev-il-tlv-1-proxy-1-i.headspin.io
dev-il-tlv-2-proxy-0-mac-i.headspin.io
dev-in-bgl-1-proxy-2-i.headspin.io
dev-in-bgl-1-proxy-4-i.headspin.io
dev-in-bgl-1-proxy-5-mac-i.headspin.io
dev-in-cjb-0-proxy-3-mac-i.headspin.io
dev-in-del-0-proxy-10-mac-i.headspin.io
dev-jp-tyo-0-proxy-17-mac-i.headspin.io
dev-jp-tyo-0-proxy-19-mac-i.headspin.io
dev-jp-tyo-1-proxy-0-mac-i.headspin.io
dev-jp-tyo-1-proxy-3-mac-i.headspin.io
dev-jp-tyo-1-proxy-7-mac-i.headspin.io
dev-jp-tyo-1-proxy-8-mac-i.headspin.io
dev-jp-tyo-1-proxy-9-mac-i.headspin.io
dev-jp-tyo-2-proxy-0-mac-i.headspin.io
dev-kr-icn-0-proxy-7-mac-i.headspin.io
dev-kr-icn-0-proxy-8-mac-i.headspin.io
dev-mx-mex-1-proxy-2-i.headspin.io
dev-mx-mex-1-proxy-3-mac-i.headspin.io
dev-ng-los-1-proxy-0-mac-i.headspin.io
dev-nl-hag-0-proxy-4-mac-i.headspin.io
dev-nz-akl-0-proxy-2-i.headspin.io
dev-pk-isl-0-proxy-4-mac-i.headspin.io
dev-pl-waw-0-proxy-0-i.headspin.io
dev-sg-sin-0-proxy-1-mac-i.headspin.io
dev-us-dal-1-proxy-0-mac-i.headspin.io
dev-us-den-0-proxy-5-mac-i.headspin.io
dev-us-mia-0-proxy-0-i.headspin.io
dev-us-mia-0-proxy-1-mac-i.headspin.io
dev-us-mia-0-proxy-3-mac-i.headspin.io
dev-us-mv-0-proxy-12-mac-i.headspin.io
dev-us-mv-0-proxy-3-mac-i.headspin.io
dev-us-nyc-1-proxy-0-mac-i.headspin.io
dev-us-pal-0-proxy-0-i.headspin.io
dev-us-pao-0-proxy-10-i.headspin.io
dev-us-pao-0-proxy-12-i.headspin.io
dev-us-pao-0-proxy-16-mac-i.headspin.io
dev-us-pao-0-proxy-18-i.headspin.io
dev-us-pao-0-proxy-2-i.headspin.io
dev-us-pao-0-proxy-22-mac-i.headspin.io
dev-us-pao-0-proxy-23-mac-i.headspin.io
dev-us-pao-0-proxy-3-i.headspin.io
dev-us-pao-0-proxy-4-i.headspin.io
dev-us-pao-0-proxy-5-i.headspin.io
dev-us-pao-0-proxy-6-mac-i.headspin.io
dev-us-pao-1-proxy-0-i.headspin.io
dev-us-pao-1-proxy-1-i.headspin.io
dev-us-pao-1-proxy-12-i.headspin.io
dev-us-pao-1-proxy-15-mac-i.headspin.io
dev-us-pao-1-proxy-16-i.headspin.io
dev-us-pao-1-proxy-2-i.headspin.io
dev-us-pao-1-proxy-20-mac-i.headspin.io
dev-us-pao-1-proxy-3-i.headspin.io
dev-us-pao-1-proxy-4-i.headspin.io
dev-us-pao-1-proxy-7-i.headspin.io
dev-us-pao-1-proxy-8-i.headspin.io
dev-us-sea-0-proxy-8-mac-i.headspin.io
dev-us-sf-0-proxy-12-mac-i.headspin.io
dev-us-sf-0-proxy-15-mac-i.headspin.io
dev-us-sf-0-proxy-16-mac-i.headspin.io
dev-us-sf-0-proxy-17-mac-i.headspin.io
dev-us-sf-0-proxy-2-mac-i.headspin.io
dev-za-jhb-1-proxy-0-mac-i.headspin.io
proxy-ae-dxb-1-i.headspin.io
proxy-au-ade-2-i.headspin.io
proxy-au-bnk-2-i.headspin.io
proxy-au-bri-3-i.headspin.io
proxy-au-lil-2-i.headspin.io
proxy-au-mbw-4-i.headspin.io
proxy-au-mel-2-i.headspin.io
proxy-au-per-2-i.headspin.io
proxy-au-syd-2-i.headspin.io
proxy-br-rio-0-i.headspin.io
proxy-ca-tor-7-i.headspin.io
proxy-cn-hk-0-i.headspin.io
proxy-cn-shg-0-i.headspin.io
proxy-cn-shg-3-i.headspin.io
proxy-de-fra-0-i.headspin.io
proxy-de-fra-9-i.headspin.io
proxy-eg-cai-0-i.headspin.io
proxy-es-bio-2-i.headspin.io
proxy-es-bio-4-i.headspin.io
proxy-fr-par-0-i.headspin.io
proxy-fr-par-7-i.headspin.io
proxy-gb-lhr-0-i.headspin.io
proxy-gb-lhr-11-i.headspin.io
proxy-gb-lhr-9-i.headspin.io
proxy-gb-oxf-0-i.headspin.io
proxy-gb-oxf-4-i.headspin.io
proxy-hk-hkg-5-i.headspin.io
proxy-hk-hkg-6-i.headspin.io
proxy-id-jk-0-i.headspin.io
proxy-id-jk-9-i.headspin.io
proxy-in-blr-0-i.headspin.io
proxy-in-blr-3-i.headspin.io
proxy-in-blr-6-i.headspin.io
proxy-in-del-7-i.headspin.io
proxy-in-dlh-1-i.headspin.io
proxy-it-mxp-2-i.headspin.io
proxy-jp-tyo-0-i.headspin.io
proxy-jp-tyo-10-i.headspin.io
proxy-jp-tyo-11-i.headspin.io
proxy-jp-tyo-14-i.headspin.io
proxy-jp-tyo-8-i.headspin.io
proxy-ke-nai-8-i.headspin.io
proxy-kh-pnh-0-i.headspin.io
proxy-kr-icn-3-i.headspin.io
proxy-mx-mex-0-i.headspin.io
proxy-mx-mex-8-i.headspin.io
proxy-mx-mex-9-i.headspin.io
proxy-my-kul-0-i.headspin.io
proxy-ph-mnl-0-i.headspin.io
proxy-ru-she-2-i.headspin.io
proxy-ru-she-4-i.headspin.io
proxy-sa-ruh-3-i.headspin.io
proxy-se-sto-3-i.headspin.io
proxy-th-bnk-0-i.headspin.io
proxy-tr-ist-0-i.headspin.io
proxy-tw-tnn-0-i.headspin.io
proxy-us-chi-0-i.headspin.io
proxy-us-den-0-i.headspin.io
proxy-us-den-3-i.headspin.io
proxy-us-la-0-i.headspin.io
proxy-us-la-2-i.headspin.io
proxy-us-mv-16-i.headspin.io
proxy-us-mv-17-i.headspin.io
proxy-us-mv-19-i.headspin.io
proxy-us-mv-2-i.headspin.io
proxy-us-mv-28-i.headspin.io
proxy-us-mv-6-i.headspin.io
proxy-us-mv-9-i.headspin.io
proxy-us-nyc-0-i.headspin.io
proxy-us-nyc-10-i.headspin.io
proxy-us-nyc-2-i.headspin.io
proxy-us-nyc-6-i.headspin.io
proxy-us-nyc-7-i.headspin.io
proxy-us-sea-0-i.headspin.io
proxy-us-sea-4-i.headspin.io
proxy-us-sea-6-i.headspin.io
proxy-us-sea-7-i.headspin.io
proxy-us-sf-0-i.headspin.io
proxy-us-sf-4-i.headspin.io
proxy-vn-hcm-2-i.headspin.io
proxy-za-jhb-4-i.headspin.io

    """
    # print(hosts)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as pool:
        for host in hosts.split():
            pool.submit(run, host)

main()



