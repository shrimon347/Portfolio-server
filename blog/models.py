from django.db import models
from django.conf import settings
# Create your models here.
class Blog(models.Model):
    COLOR_CHOICES = [
        ('#025A4E', 'green'),
        ('#EDE7DE', 'cream'),
       
    ]
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    date = models.DateField( auto_now=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    author = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    COLOR_CHOICES = [
        ('#025A4E', 'green'),
        ('#EDE7DE', 'cream'),
       
    ]
    website_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/project', default=None)
    stack_use = models.CharField(max_length=500)
    preview_url = models.URLField(max_length=500,blank=True,null=True)
    github_url = models.URLField(max_length=500,blank=True,null=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    date = models.DateField( auto_now=True)
    
    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'

    def __str__(self):
        return self.website_name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    project = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name