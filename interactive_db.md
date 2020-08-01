
```
len([d for d in r.devices if d.device_state == device_list_cache_model.DeviceState.Online])
```
Out[10]: 1395
```
len({d.hostname for d in r.devices if d.device_state == device_list_cache_model.DeviceState.Online})
```
Out[11]: 400

Sequel pro
```
select count(*) from DeviceListCache
 where device_state = 'online';
```
1843 online devices as of June 3,2020
```
select count(*) from DeviceListCache;
```
2261 - All devices
``` 
select Distinct(hostname) from DeviceListCache;
```
529 hostnames




`import headspin.model.device_list_cache_model as dlcm`

`a = dlcm.select_devices(dict(device_id=353626070791038))`
`a.devices`

```
Out[5]: 
[<DeviceInfo android device_id=353626070791038 serial=02548af4f3b04c73 hostname=dev-us-pao-1-proxy-9.headspin.io >,
 <DeviceInfo android device_id=353626070791038 serial=02548af4f3b04c73 hostname=proxy-us-den-1.headspin.io >]
```

`a = dlcm.select_devices(dict(device_id="00008030-000D49C81452802E"))`
`a.devices`


# GEOS

import headspin.env
from headspin.model import device_list_cache_model as dlcm
devices = dlcm.select_devices(dict(removed=False)).devices
geos = set([headspin.env.Host.create(device.hostname).natted_subdomain() for device in devices])
len(geos)
geos.remove('gb-oxf')

>>> from headspin.model import device_list_cache_model as dlcm
dlcm>>> dlcm.get_devices_for_host('dev-us-pao-0-proxy-26-lin.headspin.io')
[<DeviceInfo android device_id=0 serial=R3CMA0683DZ hostname=dev-us-pao-0-proxy-26-lin.headspin.io >, <DeviceInfo android device_id=0 serial=RFCN30AFA0J hostname=dev-us-pao-0-proxy-26-lin.headspin.io >]
>>> 
