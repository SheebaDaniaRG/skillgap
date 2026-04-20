from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_gap_view),
    path('trending/', views.trending_skills),
    path('roles/', views.role_explorer),
    path('city/', views.city_demand),
    path('courses/', views.courses_page),
]