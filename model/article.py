from google.appengine.ext import ndb

class Article(ndb.Model):
	username = ndb.StringProperty()
	title = ndb.StringProperty()
	text = ndb.StringProperty()
	date = ndb.DateProperty(auto_now_add=True)
