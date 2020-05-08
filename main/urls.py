from django.urls import include, path
from django.conf.urls import url
from . import api

urlpatterns = [
    path('registration/', include('rest_auth.registration.urls')),
    path('', include('rest_auth.urls')),
    url('init/', api.initialize),
]