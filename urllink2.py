from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


newurls = ""

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def urldata(urllink):
    global urls
    url =  urllink
    
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    line = 1
    tags = soup('a')
    for tag in tags:
        if line == int(position):
            urls = tag.get('href', None)
            print(urls)
            break
        line = line + 1


urls = input('Enter - ')
count = input('Enter count:')
position = input('Enter position:')

i = 1
print(urls)
while i <= int(count):
    urldata(urls)
    i = i + 1