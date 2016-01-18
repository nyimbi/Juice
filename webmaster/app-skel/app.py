"""
::Webmaster::

https://github.com/mardix/webmaster

app_{project_name}.py

This is the entry point of the application.

--------------------------------------------------------------------------------

** To serve the local development app

> webcli local -a {project_name}

#---------

** To deploy with Propel ( https://github.com/mardix/propel )

> propel -w

#---------

** To deploy with Gunicorn

> gunicorn app_{project_name}:app

"""

from webmaster import Webmaster

# Import the application's views
import application.{project_name}.views

# 'app' variable name is required if you intend to use it with 'webcli'
app = Webmaster.init(__name__, project="{project_name}")

