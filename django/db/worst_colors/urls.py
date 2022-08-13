from django.urls import path, include
from db.worst_colors import views

urlpatterns = [
    path(r'worst_colors', views.worst_color_api)
]
