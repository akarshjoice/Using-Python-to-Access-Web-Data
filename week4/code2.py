from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter Url: ")
count=input("Enter count: ")
position=input("Enter position: ")
count=int(count)
position=int(position)
i=0
while i<(count+1):
	print(url)
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
	tags = soup('a')
	#print(tags)
	sum=0
	tag=tags[position-1]
	url=tag.get('href', None)
	
	i=i+1
    # Look at the parts of a tag
    #print('TAG:', tag)
   # print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    	
    #print('Attrs:', tag.attrs)