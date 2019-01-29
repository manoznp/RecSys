from django.db import models
from tinymce.models import HTMLField

class Destination(models.Model):
    title = models.CharField(max_length=150, blank=False)
    slug = models.CharField(max_length=100, blank=False)
    image = models.FileField(upload_to="img", blank=False)
    content = HTMLField(blank=False)
    act = (("publish","Publish"),("draft", "Draft"))
    action = models.CharField(max_length=50, choices=act, default="draft")

    def __str__(self):
        return self.title


    
