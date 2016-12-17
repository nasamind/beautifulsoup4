from bs4 import BeautifulSoup

inputString = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(inputString)
comment = soup.b.string
print type(comment) # <class 'bs4.element.Comment'>
print comment,"\n" # Hey, buddy. Want to buy a used parser
print(soup.b.prettify())