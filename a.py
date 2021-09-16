# import requests

# res = requests.get('https://amazon.com')

# print(res.text)
# print(res.status_code)

import urllib.request
import re
import urllib.parse
url = 'https://www.flipkart.com/search?q=laptop'
values = {'q':'laptop'}

data  = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall('"((http|ftp)s?://.*?)"',str(respData))

# print(paragraphs)
for i in range(10,20):
    print(paragraphs[i])


