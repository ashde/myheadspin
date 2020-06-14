#!/usr/bin/env python
import sys
import re

ip = sys.argv[1]

def is_valid_ip(ip):
        m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
        return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))


if __name__ == '__main__':
        result = is_valid_ip(ip)
        print(result)
