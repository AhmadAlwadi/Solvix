'''This program will be used to fetch the random cube combiation from a 
site called cubemania; the site hosts the combination on 
"https://www.cubemania.org/puzzles/3x3x3/timer" and upon inspection it 
is stored in a class called scramble'''

#import libraries
import requests, sys, urllib.request
import bs4 as bs
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

class Client(QWebPage):
	def __init__(self, URL):
		self.app=QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.mainFrame().load(QUrl(URL))
		self.app.exec_()

	def on_page_load(self):
		self.app.quit()

URL = 'https://www.cubemania.org/puzzles/3x3x3/timer'
client_response=Client(URL)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'html.parser')
placeholder = soup.find(id='content')
print(placeholder)
