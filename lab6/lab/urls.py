from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('details/<int:student_id>/', views.details, name='details'),
]