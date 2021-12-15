from django.contrib import admin
from django.urls import path
from appadmin import views


urlpatterns = [
    path('faculty_profile/', views.faculty_profile, name='faculty_profile'),
    path('manage_student_faculty/', views.manage_student_faculty, name='manage_student_faculty'),
    path('manage_student_cdc/', views.manage_student_cdc, name='manage_student_cdc'),
    path('manage_faculty_cdc/', views.manage_faculty_cdc, name='manage_faculty_cdc'),
    path('view_faculty_cdc/', views.view_faculty_cdc, name='view_faculty_cdc'),
    path('view_student_cdc/', views.view_student_cdc, name='view_student_cdc'),
    path('view_student_faculty/', views.view_student_faculty, name='view_student_faculty'),
    
]