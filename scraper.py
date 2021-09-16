from html.parser import HTMLParser
import urllib.request
import re
import urllib.parse

class LinksParser1(HTMLParser):
  recording = 0
  data = []
  def _init_(self):
    HTMLParser._init_(self)

  def handle_starttag(self, tag, attributes):
    if tag != 'div':
      return
    if self.recording:
      self.recording += 1
      return
    for name, value in attributes:
      if name == 'class' and value == '_4rR01T':
        break
    else:
      return

    self.recording = 1

  def handle_endtag(self, tag):
   if tag == 'div' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)


class LinksParser2(HTMLParser):
  recording = 0
  data = []
  def _init_(self):

    HTMLParser._init_(self)

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            for name,value in attrs:
                if name == "href"  :
                    print ("https://www.flipkart.com"+value)

    self.recording = 1

  def handle_endtag(self, tag):
   if tag == 'div' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)

class Scrap():
    
    # def scapper(link_name, product):
    def __init__(self,link_name, product):
        values = {'q':product}

        data  = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        url = str("https://www."+link_name+".com/search?"+"q="+product)
        print(url)
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        
    
        def products():
            print("Products Name ")
            parser1 = LinksParser1()
            parser1.feed(respData.decode("UTF-8"))
            data  = parser1.data
            for i in data:
                print(i)

        def links1():
            paragraphs = re.findall('"((http|ftp)s?://.*?)"',str(respData))

            print(paragraphs)
            for i in range(10,20):
                print(paragraphs[i])

        def links():
        
            print("\n\n\n  LINKS \n\n\n\n")
            parser2 = LinksParser2()
            parser2.feed(respData.decode("UTF-8"))
            data1  = parser2.data
            for i in data1:
                print(i)

        # Products Name         
        products()

        # Links for Products as I've used Html parser I am not able to fectg
        # links()

        # another way to fetch links 
        links1()
        
        

# Pass name of website and Products
obj = Scrap("flipkart","laptop")




