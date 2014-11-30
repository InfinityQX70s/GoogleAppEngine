import jinja2
import os
import webapp2
import logging
import re
import hashlib

from google.appengine.ext import ndb
from model.user import User

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/blog/views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)     # See OS path

def checkcookies(self):
	return False if self.request.cookies.get('user_id') is None else True

def validation(self):
	return True if re.search(r'^[a-zA-Z0-9]+[\'\+\_\-\.a-zA-Z0-9]*\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*\.[a-zA-Z]+$',self) else False

class RegisterUser(webapp2.RequestHandler):

	def get(self):
		templatevalues = {
            'user_log' : checkcookies(self),
		} 
		template = jinja_environment.get_template('register.html')
		self.response.out.write(template.render({'templatevalues':templatevalues}))

	def post(self):
		isUser = User.query(User.username == self.request.get('username')).get()
		if((isUser is None) and (self.request.get('confirm') == self.request.get('password')) and validation(self.request.get('email'))):
			hashsum = hashlib.md5(self.request.get('password')).hexdigest()
			users = User(username = self.request.get('username'),
                    	password=hashsum )
			users.put()
			return webapp2.redirect('/')
		else:
			templatevalues = {
            	'user_log' : checkcookies(self),
			} 
			template = jinja_environment.get_template('error.html')
			self.response.out.write(template.render({'templatevalues':templatevalues}))


class LoginUser(webapp2.RequestHandler):
	
	def get(self):
		templatevalues = {
            'user_log' : checkcookies(self),
		} 
		template = jinja_environment.get_template('login.html')
		self.response.out.write(template.render({'templatevalues':templatevalues}))

	def post(self):
		username = self.request.get('username')
		hashsum = hashlib.md5(self.request.get('password')).hexdigest()
		userinfo = User.query(User.username == username).get()
		templatevalues = {
		 		'user_log' : checkcookies(self),
		} 
		if (userinfo == None):
			template = jinja_environment.get_template('error.html')
			self.response.out.write(template.render({'templatevalues':templatevalues}))
		else:
			usercook = str(userinfo.key.id())
			if userinfo.password == hashsum:
				self.response.set_cookie('user_id', usercook, path='/')
				return webapp2.redirect('/', response=self.response)
			else:
				template = jinja_environment.get_template('error.html')
				self.response.out.write(template.render({'templatevalues':templatevalues}))

class LogoutUser(webapp2.RequestHandler):

	def get(self):
		logging.info(self.request.cookies.get('user_id'))
		self.response.delete_cookie('user_id')
		return webapp2.redirect('/', response=self.response)
