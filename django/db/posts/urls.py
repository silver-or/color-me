from django.urls import path
from db.posts import views

urlpatterns = [
    path(r'posts', views.post_api)
]
