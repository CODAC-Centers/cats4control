from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from django.db import models
from .models import Event, Project, Researcher, Reference

def home(request):
    """Home page view"""
    # Get featured events
    featured_events = Event.objects.filter(is_featured=True).order_by('start_date')[:3]
    
    # Get active projects
    active_projects = Project.objects.filter(status='active', is_public=True)[:5]
    
    # Get upcoming events
    upcoming_events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')[:3]
    
    context = {
        'featured_events': featured_events,
        'active_projects': active_projects,
        'upcoming_events': upcoming_events,
    }
    
    return render(request, 'main/home.html', context)

def events_list(request):
    """List all events"""
    events = Event.objects.all().order_by('-start_date')
    return render(request, 'main/events_list.html', {'events': events})

def event_detail(request, event_id):
    """Event detail page"""
    event = get_object_or_404(Event, id=event_id)
    talks = event.talks.all().order_by('start_time')
    
    # Collect all unique references from all talks
    event_references = Reference.objects.filter(
        talks__event=event
    ).distinct().order_by('-year', 'title')
    
    return render(request, 'main/event_detail.html', {
        'event': event, 
        'talks': talks,
        'event_references': event_references
    })

def projects_list(request):
    """List all public projects"""
    projects = Project.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'main/projects_list.html', {'projects': projects})

def project_detail(request, project_id):
    """Project detail page"""
    project = get_object_or_404(Project, id=project_id, is_public=True)
    return render(request, 'main/project_detail.html', {'project': project})

def researchers_list(request):
    """List all active researchers"""
    researchers = Researcher.objects.filter(is_active=True).order_by('name')
    return render(request, 'main/researchers_list.html', {'researchers': researchers})

def researcher_detail(request, researcher_id):
    """Researcher profile page"""
    researcher = get_object_or_404(Researcher, id=researcher_id, is_active=True)
    projects = Project.objects.filter(
        collaborators=researcher,
        is_public=True
    ).distinct()
    return render(request, 'main/researcher_detail.html', {
        'researcher': researcher,
        'projects': projects
    })

def references_list(request):
    """List all references"""
    references = Reference.objects.all().order_by('-year', 'title')
    return render(request, 'main/references_list.html', {'references': references})

def acc2025_view(request):
    """View for the ACC 2025 workshop"""
    return render(request, 'main/acc2025.html')
