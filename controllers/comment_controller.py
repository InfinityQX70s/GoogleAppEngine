import jinja2
import os
import webapp2
import logging

from google.appengine.ext import ndb
from model.coment import Coment


class CreateComent(webapp2.RequestHandler):

    def post(self, num_com):
        num_com = int(num_com)
        coments = Coment(username = "test",
                    title=self.request.get('title'),
                    text=self.request.get('text'),
                    forarticle = num_com)
        coments.put()
        return webapp2.redirect('/show/'+str(num_com))

class DeleteComent(webapp2.RequestHandler):

    def get(self,num_art, del_com):
        ndb.Key('Coment',int(del_com)).delete()
        return webapp2.redirect('/show/'+str(num_art))