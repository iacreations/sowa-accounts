from django.urls import path
from . import views
appname='sowaAuth'
urlpatterns = [
    path('register', views.register_user, name='register')
]
