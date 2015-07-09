from lxml import html
import IPython
import urllib2
from bs4 import BeautifulSoup

"""
Test GET request and parsing in real-time
"""
req = 'https://google.com'
s = urllib2.urlopen(req).read()
soup = BeautifulSoup(s, "lxml")



# Open pre-stored HTML file for parsing
f = open('../data/aboutus.txt', 'r')
s = f.read()

# Parse HTML with Python's BeautifulSoup library
soup = BeautifulSoup(s, "lxml")
# Find spans of class img-container caption
mySpans = soup.findAll('span',{'class':'img-container caption'})
N = len(mySpans)
print 'There are ' + str(N) + ' people on the prism team. They are: '
# Print the name and position in each span
for span in mySpans:
	print '\t' + span.find('p',{'class':'bold'}).text + ', ' + span.find('p',{'class':'lead'}).text



