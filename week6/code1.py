import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
import json

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


url=input("Enter location: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urlopen(url, context=ctx).read()
data=data.decode()
info = json.loads(data)
print('User count:', len(info))
sum=0
for item in info['comments']:
    sum+=int(item['count'])
print(sum)