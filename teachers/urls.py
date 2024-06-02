from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProffesorList.as_view())
]