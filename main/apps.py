from django.apps import AppConfig
from .models import *
import json
from django.contrib.auth import User
from django.http import HttpResponse
from django.http import JsonResponse

class MainConfig(AppConfig):
    name = 'main'
