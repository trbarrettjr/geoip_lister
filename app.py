#!/usr/bin/python3
import geoip2.database

space = ' '

reader = geoip2.database.Reader('/app/GeoLite2-ASN.mmdb')

bad_ips = []

with open('ip_list.txt', 'r') as file:
  for ip in file:
    try:
      response = reader.asn(ip.strip())
      print(f'IP: {ip.strip()}' + space * (25 - len(f'IP: {ip.strip()}')) + f'ISP: {response.autonomous_system_organization}')
    except:
      bad_ips.append(ip.strip())

  if bad_ips:
    print()
    print("List of Bad IP's")
    for ip in bad_ips:
      print(f"Bad Reporting: {ip}")
