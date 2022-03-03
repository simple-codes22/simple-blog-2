from django.db import models
from django.contrib.auth.models import User

class article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=700, blank=False, editable=True)
    subtitle = models.TextField(unique=True, blank=True, editable=True)
    summary_intro = models.TextField(verbose_name="Introduction", max_length=500, unique=True, null=False, blank=False, editable=True, default='')
    body = models.TextField(unique=True, blank=False, null=False, editable=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Title: {self.title} By: {self.owner}"

