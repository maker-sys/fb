"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

        # Add your project's root directory to the Python path
        path = '/fb/misite/mysite/wsgi.py' # Replace with your actual path
        if path not in sys.path:
            sys.path.insert(0, path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
