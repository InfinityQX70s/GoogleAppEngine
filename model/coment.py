from google.appengine.ext import ndb

class Coment(ndb.Model):
	username = ndb.StringProperty()
	title = ndb.StringProperty()
	text = ndb.StringProperty()
	forarticle = ndb.IntegerProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)