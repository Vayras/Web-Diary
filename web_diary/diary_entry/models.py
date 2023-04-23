from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mood(models.Model):
    name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True, blank=True)

    # "models.SET_NULL" means that when you delete a particular mood, its value will get equal to null. And "blank=True" ensures that we can submit an empty field in the form.

    def __str__(self):
        return f"{self.date_created.date()}"