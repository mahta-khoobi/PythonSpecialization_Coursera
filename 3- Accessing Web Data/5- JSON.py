import urllib.request 
import json
import ssl
##The program will prompt for a URL, read the JSON data from that URL using
##urllib and then parse and extract the comment counts from the JSON data,
##compute the sum of the numbers in the file and enter the sum below:
##Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
##Actual data: http://py4e-data.dr-chuck.net/comments_792632.json (Sum ends with 12)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Retriving...')
connection = urllib.request.urlopen(url)
data=connection.read().decode()
js= json.loads(data)



count = 0

for item in js['comments']:
    count = count + int(item['count'])

print('count:', count)
