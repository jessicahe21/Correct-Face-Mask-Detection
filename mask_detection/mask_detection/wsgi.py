# how our python web application and the server communicates 
"""
WSGI config for cpen_291_mask_detection project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpen_291_mask_detection.settings')

application = get_wsgi_application()
