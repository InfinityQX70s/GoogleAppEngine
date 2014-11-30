from google.appengine.ext import ndb

class Coment(ndb.Model):
	username = ndb.StringProperty()
	text = ndb.StringProperty()
	forarticle = ndb.IntegerProperty()
	date = ndb.DateProperty(auto_now_add=True)