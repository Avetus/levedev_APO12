"""
WSGI config for mysite1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('D:/Django-1.7/')
sys.path.append('D:/mysite1/mysite1/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite1.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()