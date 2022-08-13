from django.urls import path, include
from db.youtubers import views

urlpatterns = [
    path(r'youtubers', views.youtuber_api)
]
