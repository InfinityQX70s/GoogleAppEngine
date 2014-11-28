import jinja2
import os
import webapp2
import logging
import hashlib

from google.appengine.ext import ndb
from model.user import User

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/blog/views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)     # See OS path

class RegisterUser(webapp2.RequestHandler):

	def get(self):
		template = jinja_environment.get_template('register.html')
		self.response.out.write(template.render({}))

	def post(self):
		hashsum = hashlib.md5(self.request.get('password')).hexdigest()
		users = User(username = self.request.get('username'),
                    password=hashsum )
		users.put()
		return webapp2.redirect('/')

class LoginUser(webapp2.RequestHandler):
	
	def get(self):
		template = jinja_environment.get_template('login.html')
		self.response.out.write(template.render({}))

	def post(self):
		username = self.request.get('username')
		hashsum = hashlib.md5(self.request.get('password')).hexdigest()
		userinfo = User.query(User.username == username).get()
		usercook = str(userinfo.key.id())
		if userinfo.password == hashsum:
			#self.response.set_cookie('name', usercook, expires=datetime.datetime.now(), path='/', domain='.localhost')
			self.response.set_cookie('user_id', usercook, path='/')
			template = jinja_environment.get_template('login.html')
			self.response.out.write(template.render({}))
			#return webapp2.redirect('/')
		else:
			template = jinja_environment.get_template('error.html')
			self.response.out.write(template.render({}))

class LogoutUser(webapp2.RequestHandler):

	def get(self):
		logging.info(self.request.cookies.get('user_id'))
		self.response.delete_cookie('user_id')
		#return webapp2.redirect('/')
