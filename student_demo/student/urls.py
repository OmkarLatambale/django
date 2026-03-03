from django.contrib import admin
from django.urls import path,include
from .views import StudentListCreateView

urlpatterns = [
    path('students/',StudentListCreateView.as_view(),name='student-list')
]