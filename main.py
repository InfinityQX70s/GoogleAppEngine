import webapp2
from controllers.article_controller import CreateArticle, MainPage, DeleteArticle, ShowArticle
from controllers.comment_controller import CreateComent, DeleteComent
from controllers.user_controller import RegisterUser, LoginUser, LogoutUser


app = webapp2.WSGIApplication([
    	webapp2.Route(r'/', handler=MainPage, name=''),
		webapp2.Route(r'/login', handler=LoginUser, name=''),
		webapp2.Route(r'/logout', handler=LogoutUser, name=''),
		webapp2.Route(r'/register', handler=RegisterUser, name=''),
    	webapp2.Route(r'/create', handler=CreateArticle, name=''),
    	webapp2.Route(r'/delete/<article_id:\d+>', handler=DeleteArticle, name=''),
    	webapp2.Route(r'/<num_art:\d+>', handler=ShowArticle, name=''),
    	webapp2.Route(r'/<num_com:\d+>/create', handler=CreateComent, name=''),
    	webapp2.Route(r'/<num_art:\d+>/delete/<del_com:\d+>', handler=DeleteComent, name=''),
	], debug=True)
