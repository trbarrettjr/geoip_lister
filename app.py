#!/usr/bin/python3
import geoip2.database

space = ' '

reader = geoip2.database.Reader('/app/GeoLite2-ASN.mmdb')

with open('ip_list.txt', 'r') as file:
  for ip in file:
    response = reader.asn(ip.strip())
    print(f'IP: {ip.strip()}' + space * (25 - len(f'IP: {ip.strip()}')) + f'ISP: {response.autonomous_system_organization}')
