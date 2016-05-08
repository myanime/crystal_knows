from __future__ import unicode_literals

from django.db import models

class Scraper(models.Model):
    first_name = models.CharField(max_length=100, default='Maria')
    last_name = models.CharField(max_length=100, default='Ivanova')
    about_person = models.TextField()
