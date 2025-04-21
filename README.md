# geoip_lister

The goal of this project:

1. Get a list of ip addresses
2. Check them against Maxmind's ASN database

The goal is to gain knowledge of the ip addresses that are connecting to my personal firewall.

For obvious reasons, I didn't include the Maxmind GeoIP database file in the repository.  You can signed up for an account at [https://maxmind.com](https://maxmind.com)

## Running

```bash
docker run --rm -it -v ./ip_list.txt:/app/ip_list.txt geoip
```
