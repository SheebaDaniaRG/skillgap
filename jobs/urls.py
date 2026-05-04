from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_gap_view, name='dashboard'),
    path('trending/', views.trending_skills, name='trending'),
    path('roles/', views.role_explorer, name='roles'),
    path('city/', views.city_demand, name='city'),
    path('courses/', views.courses_page, name='courses'),
]