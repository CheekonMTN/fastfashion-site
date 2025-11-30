"""
WSGI config for fastfashion project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fastfashion.settings")

application = get_wsgi_application()

# --- HARD OVERRIDE ALLOWED_HOSTS TO FIX DisallowedHost ON EB ---
# This ensures ALLOWED_HOSTS is set even if environment variable fails
from django.conf import settings

# Always ensure EB domain is in ALLOWED_HOSTS
eb_domain = "fastfashion-env.eba-av2bdkme.us-east-1.elasticbeanstalk.com"
if eb_domain not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append(eb_domain)
    
# Also ensure localhost is there
if "localhost" not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append("localhost")
if "127.0.0.1" not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append("127.0.0.1")
