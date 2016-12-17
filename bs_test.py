from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r)
#print type(soup)
#print soup.prettify()
letters = soup.find_all('div', class='ec_statements')

print type(letters)
print len(letters)
#print letters
#all_div = soup.find("div", {"class": "ec_statements"})
#div = soup.find(id="legalert_title")
#print div