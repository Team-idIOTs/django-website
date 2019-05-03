from django.db import models

# Create your models here.
class Cues(models.Model):
    name = models.CharField(max_length=25)

class Reminders(models.Model):
    name = models.CharField(max_length=25)