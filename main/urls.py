from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_list, name='events_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('researchers/', views.researchers_list, name='researchers_list'),
    path('researchers/<int:researcher_id>/', views.researcher_detail, name='researcher_detail'),
    path('references/', views.references_list, name='references_list'),
    path('acc2025/', views.acc2025_view, name='acc2025'),
]