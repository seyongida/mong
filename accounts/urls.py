# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/signup2/', signup2, name='signup2'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
]