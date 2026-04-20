from django.contrib import admin
from django.urls import path, include
from jobs.views import skill_gap_view   # 👈 IMPORT YOUR VIEW

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 THIS FIXES YOUR ERROR
    path('', skill_gap_view, name='home'),

    # existing
    path('jobs/', include('jobs.urls')),
]