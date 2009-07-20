import os

from google.appengine.ext.webapp import template
from google.appengine.api import users

import config

class Page:

    def render(self, handler, template_file, template_values={}):
        """Render a template"""
        values = {'user': users.get_current_user(),
                  'user_is_admin': users.is_current_user_admin(),
                 }

        values.update({'settings': config.SETTINGS})
        values.update(template_values)

        template_path = os.path.join(config.APP_ROOT_DIR, template_file)
        handler.response.out.write(template.render(template_path, values))

    def render_error(self, handler, error):
        """Render an error page"""
        # TODO: Add more error pages for 403, 500, etc.
        valid_errors = [404]

        # If the error code given is not in the list then default to 404
        if error not in valid_errors:
            error = 404

        # Set the error code on the handler
        handler.error(error)

        self.render(handler, 'templates/error/%d.html' % error, {})
