# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# This file trys to find the span tags and sum all the numbers which are
# the contents off this tag

# source:
# http://py4e-data.dr-chuck.net/comments_42.html : count: 2553
# http://py4e-data.dr-chuck.net/comments_792629.html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the span tags
count = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    count= count+ int(tag.contents[0])

    #print('Attrs:', tag.attrs)
print('count:', count)
