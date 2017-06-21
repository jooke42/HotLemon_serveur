"""
WSGI config for hotlemon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

<<<<<<< HEAD
#from django.core.handlers.wsgi import WSGIHandler
=======
from django.core.handlers.wsgi import WSGIHandler
>>>>>>> 0b2d8f222e879314de833d4ebb7eedf7f01e75f9
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotlemon.settings")

application = get_wsgi_application()
#application = WSGIHandler()
