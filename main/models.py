from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Researcher(models.Model):
    """Researcher profiles in the community"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    institution = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True,max_length=2000)
    website = models.URLField(blank=True)
    lab_website = models.URLField(blank=True)
    lab_name = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='researcher_photos/', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.institution}"

class Reference(models.Model):
    """Database of papers and books"""
    REFERENCE_TYPES = [
        ('paper', 'Paper'),
        ('book', 'Book'),
        ('thesis', 'Thesis'),
        ('preprint', 'Preprint'),
        ('journal_article', 'Journal Article'),
        ('conference_proceedings', 'Conference Proceedings'),
        ('book_chapter', 'Book Chapter'),        
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=1000,help_text="Comma-separated list of authors in the format 'Lastname, Firstname.'")
    year = models.IntegerField()
    reference_type = models.CharField(max_length=40, choices=REFERENCE_TYPES)
    journal = models.CharField(max_length=200, blank=True)
    volume = models.CharField(max_length=50, blank=True)
    pages = models.CharField(max_length=50, blank=True)
    doi = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    pdf_file = models.FileField(upload_to='references/', blank=True)
    abstract = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    added_by = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', 'title']
    
    def __str__(self):
        return f"{self.title} ({self.year})"

class Project(models.Model):
    """Collaborative research projects"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    collaborators = models.ManyToManyField(Researcher, related_name='collaborating_projects', blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ], default='active')
    image = models.ImageField(upload_to='project_images/', blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    """Events and conferences"""
    EVENT_TYPES = [
        ('workshop', 'Workshop'),
        ('tutorial', 'Tutorial'),
        ('special_session', 'Special Session'),
        ('session', 'Session'),
        ('conference', 'Conference'),
        ('meetup', 'Meet-up'),
        ('seminar', 'Seminar'),
    ]
    
    title = models.CharField(max_length=300)
    long_title = models.CharField(max_length=500, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='seminar')
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200, blank=True)
    room = models.CharField(max_length=100, blank=True)
    registration_url = models.URLField(blank=True)
    organizers = models.ManyToManyField(Researcher, related_name='organized_events', blank=True)
    image = models.ImageField(upload_to='event_images/', blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} - {self.start_date.strftime('%Y-%m-%d')}"

class Talk(models.Model):
    """Talks within events"""
    TALK_TYPES = [
        ('talk', 'Talk'),
        ('panel', 'Panel'),
        ('opening', 'Opening'),
        ('closing', 'Closing'),
        ('break', 'Break'),
        ('demo', 'Demo'),
    ]
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='talks')
    title = models.CharField(max_length=300)
    talk_type = models.CharField(max_length=20, choices=TALK_TYPES, default='talk')
    speaker = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    additional_speakers = models.ManyToManyField(Researcher, blank=True, related_name='additional_speakers')
    abstract = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    slides = models.FileField(upload_to='talk_slides/', blank=True)
    video_url = models.URLField(blank=True)
    references = models.ManyToManyField(Reference, blank=True, related_name='talks')
    
    class Meta:
        ordering = ['start_time']
    
    def __str__(self):
        return f"{self.title} - {self.speaker.name}"
