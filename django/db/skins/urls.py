from django.urls import path
from db.skins import views

urlpatterns = [
    path(r'skins', views.skin_api)
]
