import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'lps_django_2024.settings'
application = get_wsgi_application()
