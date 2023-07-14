from django.http import HttpResponse
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application

def index(request):
    return HttpResponse('Hello, World!')

urlpatterns = [
    url(r'^$', index),
]

application = get_wsgi_application()
