from django.urls import path
from db.best_colors import views

urlpatterns = [
    path(r'best_colors', views.best_color_api)
]
