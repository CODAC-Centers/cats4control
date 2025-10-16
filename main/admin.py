from django.contrib import admin
from .models import (
    Researcher, Reference, Project, Event, Talk
)

@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'institution', 'created_at']
    search_fields = ['name', 'email', 'institution', 'bio']
    ordering = ['name']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'year', 'reference_type', 'added_by']
    list_filter = ['reference_type', 'year', 'added_by']
    search_fields = ['title', 'authors', 'keywords', 'abstract']
    ordering = ['-year', 'title']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_date', 'is_public']
    list_filter = ['status', 'is_public', 'start_date']
    search_fields = ['name', 'description']
    filter_horizontal = ['collaborators']
    ordering = ['-start_date']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'location', 'is_featured']
    list_filter = ['is_featured', 'start_date', 'location']
    search_fields = ['title', 'description', 'location']
    filter_horizontal = ['organizers']
    ordering = ['-start_date']

@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ['speaker', 'event', 'start_time', 'end_time', 'talk_type']
    list_filter = ['event', 'start_time', 'speaker', 'talk_type']
    search_fields = ['abstract', 'speaker__name']
    ordering = ['start_time']
