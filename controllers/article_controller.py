import jinja2
import os
import webapp2
import logging
from datetime import datetime

from google.appengine.ext import ndb
from model.article import Article
from model.coment import Coment
from model.user import User


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/blog/views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)     # See OS path

def checkcookies(self):
    return False if self.request.cookies.get('user_id') is None else True


class MainPage(webapp2.RequestHandler):

    def get(self):
        articles = Article.query().order(-Article.date)
        templatevalues = {
            'articles': articles,
            'user_log' : checkcookies(self),
        }  
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))

    def post(self):
        datearticle = self.request.get('datearticle')
        datearticle = datetime.strptime(datearticle+' 00:00:00', '%m/%d/%Y %H:%M:%S')
        articles = Article.query(Article.date == datearticle).order(-Article.date)
        templatevalues = {
            'articles': articles,
            'user_log' : checkcookies(self),
        }  
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))


class CreateArticle(webapp2.RequestHandler):

    def post(self):
        user_id = self.request.cookies.get('user_id')
        user_id = int(user_id)
        user_info = ndb.Key('User',user_id).get()
        commit = Article(username = user_info.username,
                    title=self.request.get('title'),
                    text=self.request.get('text'))
        commit.put()
        return webapp2.redirect('/')

    def get(self):
        #logging.info(os.path.join(os.path.dirname(__file__))
        articles = Article.query().order(-Article.date)
        templatevalues = {
            'user_log' : checkcookies(self),
        }
        template = jinja_environment.get_template('create.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))


class DeleteArticle(webapp2.RequestHandler):

    def get(self, article_id):
        ndb.Key('Article',int(article_id)).delete()
        return webapp2.redirect('/')


class ShowArticle(webapp2.RequestHandler):

    def get(self, num_art):
        num_art = int(num_art)
        article = ndb.Key('Article',num_art).get()
        logging.info(article)
        if (article is not None):
            coments = Coment.query(Coment.forarticle == num_art).order(-Coment.date)
            templatevalues = {
                'articles' : article,
                'coments' : coments,
                'user_log' : checkcookies(self),
            }
            template = jinja_environment.get_template('show.html')
            self.response.out.write(template.render({'templatevalues':templatevalues}))
        else:
            self.abort(404)
