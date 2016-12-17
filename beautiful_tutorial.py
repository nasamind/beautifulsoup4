hari_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(hari_doc, 'html.parser')

print(soup.prettify())
print "printing link........"
for link in soup.find_all('a'):
    print link.get('href')

print "printing id.........."
for link in soup.find_all('a'):
    print link.get('id')

print "printing text........"
for link in soup.find_all('a'):
    print link.get_text()

print "printing class name........"
for link in soup.find_all('a'):
    print link.get('class')

print "all text from page........"
print soup.get_text()

print soup.a # print first tag <a....<a/>

print  soup.find_all('a') # all tag name start with <a..</a>
all_a_tag = soup.find_all('a')

# extracting each attributes inside tagname <tag-name attribute1='attrValue' attribute2='attrValue'..></tagname>
for a_tag in all_a_tag:
    print "input string : ",a_tag
    print "1    :   ",a_tag.get_text()
    # printing tag name i.e. a , div..etc
    print "2    :   ",a_tag.name
    # attributed inside tag a
    print "3    :   ",a_tag['href']
    print "4    :   ",a_tag['class']
    print "5    :   ",a_tag['id']
    # all attributed together in a dictionary form
    print "6    :   ",a_tag.attrs,"\n"

# deletion operation
temp = all_a_tag
for a_tag in temp:
    print "input string : ",a_tag
    del a_tag['class']
    del a_tag['id']
    print "1    :   ",a_tag
    del a_tag['href']
    print "2    :   ",a_tag