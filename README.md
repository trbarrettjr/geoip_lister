# geoip_lister

The goal of this project:

1. Get a list of ip addresses
2. Check them against Maxmind's ASN database

The goal is to gain knowledge of the ip addresses that are connecting to my personal firewall.

For obvious reasons, I didn't include the Maxmind GeoIP database file in the repository.  You can signed up for an account at [https://maxmind.com](https://maxmind.com)

### Updates

Updated to consider the following:

1. Maxmind's database is updating; therefore good idea not the build into the docker image.
2. Therefore map the database file into the volume command (as seen below).

## Running - Docker CLI

```sh
docker run --rm -it -v ./GeoLite2-ASN.mmdb:/app/GeoLite2-ASN.mmdb -v ./ip_list.txt:/app/ip_list.txt geoip
```
