from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True)
    mood = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField()

    # "models.SET_NULL" means that when you delete a particular mood, its value will get equal to null. And "blank=True" ensures that we can submit an empty field in the form.

    def __str__(self):
        return f"{self.date_created.date()}"