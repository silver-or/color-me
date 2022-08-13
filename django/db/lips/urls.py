from django.urls import path
from db.lips import views

urlpatterns = [
    path(r'lips', views.lip_api)
]
