"""Simple abstraction over requests and bs4"""

import requests, time
from datetime import datetime
from bs4 import BeautifulSoup

class Browser:
	"""A browser for handling requests"""
	session = None
	headers = None
	def __init__(self):
		"""Constructor"""
		self.session = requests.Session()
		self.headers = {}
	def get(self, url):
		"""Do a get request and return response"""
		return self.session.get(url).text
	def post(self, url, data={}):
		"""Do a post"""
		return self.session.post(url, data=data, headers=self.headers).text
	def login():
		"""Login to a site given the login url and data"""
		return self.session.post(url, data=data, headers=self.headers).text

