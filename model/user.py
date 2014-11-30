from google.appengine.ext import ndb

class User(ndb.Model):
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	date = ndb.DateProperty(auto_now_add=True)