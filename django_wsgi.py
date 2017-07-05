import os  
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'dog.settings'  
import django.core.handlers.wsgi  
 
if django.VERSION < 1.7:
    from django.core.handlers.wsgi import WSGIHandler
    application = WSGIHandler()
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()