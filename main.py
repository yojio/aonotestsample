# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import os
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainPage(BaseHandler):


    def get(self):
        self.render("main.html")

class SayPage(webapp2.RequestHandler):


    def get(self):
        logging.critical("============= /say ==============")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('ごめんなさい')


application = webapp2.WSGIApplication([
                                      ('/', MainPage),
                                      ('/say', SayPage)
                                      ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
