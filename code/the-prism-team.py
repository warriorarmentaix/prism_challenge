from lxml import html
import IPython
import urllib2
from bs4 import BeautifulSoup

"""

"""
req = 'https://yahoo.com'
s = urllib2.urlopen(req).read()
soup = BeautifulSoup(s, "lxml")

f = open('../data/aboutus.txt', 'r')
s = f.read()

soup = BeautifulSoup(s, "lxml")
mySpans = soup.findAll('span',{'class':'img-container caption'})
N = len(mySpans)
print 'There are ' + str(N) + ' people on the prism team. They are: '

for span in mySpans:
	print '\t' + span.find('p',{'class':'bold'}).text + ', ' + span.find('p',{'class':'lead'}).text



