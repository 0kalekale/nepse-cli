from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(data)        
html = open("/tmp/stonk.html", "r").read()
parse = MyHTMLParser()
parse.feed(html)
