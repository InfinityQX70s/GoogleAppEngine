import jinja2
import os
import webapp2
import logging

from google.appengine.ext import ndb
from model.coment import Coment
from model.user import User


class CreateComent(webapp2.RequestHandler):

    def post(self, num_com):
        num_com = int(num_com)
        user_id = self.request.cookies.get('user_id')
        user_id = int(user_id)
        user_info = ndb.Key('User',user_id).get()
        coments = Coment(username = user_info.username,
                    text=self.request.get('text'),
                    forarticle = num_com)
        coments.put()
        return webapp2.redirect('/'+str(num_com))

class DeleteComent(webapp2.RequestHandler):

    def get(self,num_art, del_com):
        ndb.Key('Coment',int(del_com)).delete()
        return webapp2.redirect('/'+str(num_art))