from django.urls import path
from db.users import views

urlpatterns = [
    path(r'join', views.join),
    path(r'login', views.login),
    path(r'logout', views.logout)
]