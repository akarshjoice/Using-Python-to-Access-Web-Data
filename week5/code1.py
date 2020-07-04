import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl


# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


url=input("Enter location: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ul = urlopen(url, context=ctx).read()
ul=ul.decode()
tree = ET.fromstring(ul)
lis = tree.findall('.//comment')
print(lis)
sum=0
for ele in lis:
    sum+=int(ele.find('count').text)
print(sum)


