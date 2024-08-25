
import os
import sys
print(sys.path)
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopers.settings')

application = get_asgi_application()
