from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('registerCourse/', views.registerCourse),
    path('editCourse/<code>', views.editCourse ),
    path('editTheCourse/', views.editTheCourse),
    path('deleteCourse/<code>', views.deleteCourse),
]