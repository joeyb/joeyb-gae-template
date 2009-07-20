#!/usr/bin/env python
#

import config
import os
import sys

# Force sys.path to have our own directory first, so we can import from it.
sys.path.insert(0, config.APP_ROOT_DIR)
sys.path.insert(1, os.path.join(config.APP_ROOT_DIR, 'externals'))

import wsgiref.handlers

from google.appengine.ext import webapp
from handlers import error, hello

def main():
    application = webapp.WSGIApplication([('/', hello.HelloWorldHandler),
                                          # If we make it this far then the page we are looking
                                          # for does not exist
                                          ('/.*', error.Error404Handler),
                                         ],
                                         debug=True)
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
    main()
