import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Auger_BBALL.settings")

application = get_wsgi_application()
