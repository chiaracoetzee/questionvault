"""
WSGI config for questionvault project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "questionvault.settings")

import sys
path = os.path.abspath(__file__ + "/../..")
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
