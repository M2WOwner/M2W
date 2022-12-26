from django.db import models

class Note(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=1000)
    Image = models.CharField(max_length=2083)
