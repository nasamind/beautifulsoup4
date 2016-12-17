from bs4 import BeautifulSoup

css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print css_soup.p['class'] # ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
print css_soup.p['class'] # ["body"]

id_soup = BeautifulSoup('<p id="my id"></p>')
print id_soup.p['id'] # 'my id'

# making attribute as multivalue
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
old_soup = rel_soup
print rel_soup.a['rel'] # ['index']
rel_soup.a['rel'] = ['index', 'contents'] #updating 'rel' attribute
print "original string  :   ",old_soup
print "modified attribute : ",(rel_soup.p) # <p>Back to the <a rel="index contents">homepage</a></p>