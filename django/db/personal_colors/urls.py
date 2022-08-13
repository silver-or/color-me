from django.urls import path, include
from db.personal_colors import views

urlpatterns = [
    path(r'personal_colors', views.personal_color_api)
]