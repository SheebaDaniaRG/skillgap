from django.contrib import admin
from django.urls import path, include
from users.views import login_view
from jobs import views as job_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', login_view, name='home'),

    # Main apps
    path('jobs/', include('jobs.urls')),
    path('users/', include('users.urls')),

    # Direct frontend pages
    path('dashboard/', job_views.skill_gap_view, name='dashboard'),
    path('trending/', job_views.trending_skills, name='trending'),
    path('roles/', job_views.role_explorer, name='roles'),
    path('city/', job_views.city_demand, name='city'),
    path('courses/', job_views.courses_page, name='courses'),
]