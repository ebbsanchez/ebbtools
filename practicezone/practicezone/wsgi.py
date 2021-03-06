"""
WSGI config for practicezone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

if os.getenv("THIS_ENV") == "development":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practicezone.settings')
else:
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practicezone.production_settings')

application = Cling(get_wsgi_application())
