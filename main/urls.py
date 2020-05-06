from django.conf.urls import url
from django.urls import include, path
from . import api

urlpatterns = [
    path('registration/', include('rest_auth.registration.urls')),
    url('init/', api.initialize),

]