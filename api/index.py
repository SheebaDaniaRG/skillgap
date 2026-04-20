import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillgap.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()