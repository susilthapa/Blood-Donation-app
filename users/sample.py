import requests
from ip2geotools.databases.noncommercial import DbIpCity
import pygeoip
from ip2geotools.errors import LocationError, PermissionRequiredError
import geocoder
import IP2Location

my_ip_address = requests.get('https://api.ipify.org').text
IP2LocObj = IP2Location.IP2Location()
'''
    Cache the database into memory to accelerate lookup speed.
    WARNING: Please make sure your system have sufficient RAM to use this feature.
'''
# database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"), "SHARED_MEMORY")
IP2LocObj.open("data/IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-SAMPLE.BIN")
rec = IP2LocObj.get_all()

print(rec.country_short)
print(rec.latitude)
print(rec.longitude)





# my_ip_address = requests.get('https://api.ipify.org').text
# print(f"MY IP ={my_ip_address}")
#
# g = geocoder.google('Kathandu')
# addr = g.json
# latlan = g.latlng
# print(f'ADDRESS = {addr}')
# print(f'LAT ALN  = {latlan}')

# try:
#     my_ip_address = requests.get('https://api.ipify.org').text
#     print(f"MY IP ={my_ip_address}")
#     my_key = 'AIzaSyCTOr2uNAbqo4giPny4UH6jnb6nt3nsz-4'
#     response = DbIpCity.get('my_ip_address', api_key='AIzaSyCTOr2uNAbqo4giPny4UH6jnb6nt3nsz-4')
#     # print(response)
#
# except PermissionRequiredError(LocationError):
#
#     """
#     Problem with authentication or authorization of the request.
#     Check your permission for accessing the service.
#
#     """
#
#     pass





# gip = pygeoip.GeoIP('GeoLiteCity.dat')
# print(gip)
# res = gip.record_by_addr(my_ip_address)
# print(res)