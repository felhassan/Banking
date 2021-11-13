from django.urls import path
from myapp.views import index
from myapp.views import myapp
from myapp.views import customusers
from myapp.views import users
urlpatterns = [
   path('index/', index),
   path('', myapp),
   path('customusers/', customusers),
   path('users/', users),
]