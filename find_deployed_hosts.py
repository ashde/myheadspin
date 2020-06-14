#!/usr/bin/env python
import yaml
data = {}
with open('/Users/ash/headspinio/keys/dev/pbox/host_config.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
for geo, geo_data in data.items():
    if 'hosts' in geo_data:
        try:
            for host_name, host_name_val in geo_data['hosts'].items():
                if 'deployed' in host_name_val:
                    print('FLAG:    {}: {}: deployed: {}'.format(geo, host_name, host_name_val['deployed']))
                else:
                    print('NO FLAG: {}: {}'.format(geo, host_name))
        except Exception as ex:
            print('GEO Host data is NULL: {}'.format(geo))

# if FullLoader not found
# pip install -U PyYAML
