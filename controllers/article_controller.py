import jinja2
import os
import webapp2
import logging

from google.appengine.ext import ndb
from model.article import Article
from model.coment import Coment


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/blog/views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)     # See OS path

class MainPage(webapp2.RequestHandler):

    def get(self):
        articles = Article.query().order(-Article.date)
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({'articles': articles}))


class CreateArticle(webapp2.RequestHandler):

    def post(self):
        commit = Article(username = "test",
                    title=self.request.get('title'),
                    text=self.request.get('text'))
        commit.put()
        return webapp2.redirect('/')

    def get(self):
        #logging.info(os.path.join(os.path.dirname(__file__))
        template = jinja_environment.get_template('create.html')
        self.response.out.write(template.render({}))


class DeleteArticle(webapp2.RequestHandler):

    def get(self, article_id):
        ndb.Key('Article',int(article_id)).delete()
        return webapp2.redirect('/')


class ShowArticle(webapp2.RequestHandler):

    def get(self, num_art):
        num_art = int(num_art)
        article = ndb.Key('Article',num_art).get()
        coments = Coment.query(Coment.forarticle == num_art).order(-Coment.date)
        templatevalues = {
            'articles' : article,
            'coments' : coments,
        }
        template = jinja_environment.get_template('show.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))
