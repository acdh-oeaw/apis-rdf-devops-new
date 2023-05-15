"""
WSGI config for default_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("APIS_RDF_ONTOLOGY"):
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        os.environ["DJANGO_SETTINGS_MODULE"] = os.environ.get("APIS_RDF_ONTOLOGY").replace("/", ".") + ".settings.server_settings"
if os.environ.get("DJANGO_SETTINGS_MODULE"):
    application = get_wsgi_application()
else:
    print("No DJANGO_SETTINGS_MODULE envorinment variable.")
    sys.exit()

