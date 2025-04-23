#!/usr/bin/python3
import geoip2.database

space = ' '

reader = geoip2.database.Reader('/app/GeoLite2-ASN.mmdb')

bad_ips = []

with open('ip_list.txt', 'r') as file:
  for ip in file:
    response = reader.asn(ip.strip())
    if response:
      print(f'IP: {ip.strip()}' + space * (25 - len(f'IP: {ip.strip()}')) + f'ISP: {response.autonomous_system_organization}')
    else:
      bad_ips.append(ip.strip())

  print()
  print("List of Bad IP's")
  for ip in bad_ips:
    print(f"Bad Reporting: {ip}")
