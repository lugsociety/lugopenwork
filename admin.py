from django.contrib import admin
from .models import *
#this will import all the models in admin
#this is for the admin panel

admin.site.register(CustomUser)
#custom user is registered
