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

totnum = 0
countnum = 0

tags = soup('span')
for tag in tags:
    totnum = totnum + int(tag.contents[0])
    countnum = countnum + 1

print("Count", countnum)
print("Sum", totnum)
   #http://py4e-data.dr-chuck.net/comments_42.html