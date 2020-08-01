#!/usr/bin/env python
import yaml
import argparse


# Parser for user input
cli_parser = argparse.ArgumentParser(description='Get the action to be performed.')
cli_parser.add_argument('-p', '--proxies',  help="Possible optioins:  " + \
                                                "offline, online, shared, dedicated, geo")
cli_parser.add_argument('-o', '--output',  help="Save the output" + \
                                                " to a file", action="store_true")
user_args = cli_parser.parse_args()

data = {}


def host_config_loader(filepath):
    """ Loads a yaml file """
    with open('/Users/ash/headspinio/keys/dev/pbox/host_config.yml') as fd:
        # data = yaml.load(fd, Loader=yaml.FullLoader)
        data = yaml.load(fd)

    return data


def dump_online_hosts(data):
    """ Hosts expected to be Online """

    for geo, geo_data in data.items():
        if 'hosts' in geo_data:
            try:
                for host_name, host_name_val in geo_data['hosts'].items():
                    if 'deployed' in host_name_val:
                        # print('FLAG:    {}: {}: deployed: {}'.format(geo, host_name, host_name_val['deployed']))
                        pass
                    else:
                        print('ONLINE Host: {}: {}'.format(geo, host_name))
                        hostnames.append(host_name)
                        # geos.append(geo)
            except Exception as ex:
                print('GEO Host data is NULL: {}'.format(geo))
    return hostnames

def dump_offline_hosts(data):
    """ Hosts expected to be Offline """

    for geo, geo_data in data.items():
        if 'hosts' in geo_data:
            try:
                for host_name, host_name_val in geo_data['hosts'].items():
                    if 'deployed' in host_name_val:
                        print('OFFLINE Host:    {}: {}: deployed: {}'.format(geo, host_name, host_name_val['deployed']))
                        hostnames.append(host_name)
                    else:
                        # print('NO FLAG: {}: {}'.format(geo, host_name))
                        pass
            except Exception as ex:
                print('GEO Host data is NULL: {}'.format(geo))
    return hostnames

def dump_shared_hosts(data):
    """ Lists shared hosts accross multiple orgs """

    for geo, geo_data in data.items():
        if 'hosts' in geo_data:
            try:
                for host_name, host_name_val in geo_data['hosts'].items():
                    if 'shared' in host_name_val:
                        print('Shared Host:    {}: {}'.format(geo, host_name))
                        hostnames.append(host_name)
                    else:
                        pass
            except Exception as ex:
                print('GEO Host data is NULL: {}'.format(geo))
    return hostnames

def dump_dedicated_hosts(data):
    """ Lists dedicated hosts to an Org """

    for geo, geo_data in data.items():
        if 'hosts' in geo_data:
            try:
                for host_name, host_name_val in geo_data['hosts'].items():
                    if 'shared' not in host_name_val:
                        print('Dedicated Host:    {}: {}'.format(geo, host_name))
                        hostnames.append(host_name)
                    else:
                        pass
            except Exception as ex:
                print('GEO Host data is NULL: {}'.format(geo))
    return hostnames
def dump_all_geos(data):
    """ Lists all active GEOs """

    for geo, geo_data in data.items():
        if 'hosts' in geo_data:
            try:
                for host_name, host_name_val in geo_data['hosts'].items():
                    if 'deployed' in host_name_val:
                        pass
                    else:
                        geos.append(geo)
            except Exception as ex:
                print('GEO Host data is NULL: {}'.format(geo))
    return geos


if __name__ == "__main__":
    filepath = "~/headspinio/keys/dev/pbox/host_config.yml"
    data = host_config_loader(filepath)
    hostnames = []
    geos = []


    if user_args.proxies == 'offline':
        hostnames = dump_offline_hosts(data)
    elif user_args.proxies == 'online':
        hostnames = dump_online_hosts(data)
    elif user_args.proxies == 'shared':
        hostnames = dump_shared_hosts(data)
    elif user_args.proxies == 'dedicated':
        hostnames = dump_dedicated_hosts(data)
    elif user_args.proxies == 'geo':
        geos = dump_all_geos(data)

    if len(geos) != 0:
        geos.sort()
        print(len(set(geos)))
        print ( "Total GEOS ============" + "\n")
        print(set(geos))

    else:
        for host in sorted(hostnames):
            print(user_args.proxies + ": " + host)

        if user_args.output:
            status = user_args.proxies
            with open(status, "w") as outfile:
                for host in sorted(hostnames):
                    outfile.write(status + ": " + host + "\n")
