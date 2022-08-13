from django.urls import path
from db.hairs import views

urlpatterns = [
    path(r'hairs', views.hair_api)
]
