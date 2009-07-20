from google.appengine.ext import webapp

import view

class HelloWorldHandler(webapp.RequestHandler):

    def get(self):
        page = view.Page()
        page.render(self, 'templates/hello/index.html', {})
