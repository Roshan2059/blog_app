from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    topic = models.CharField(max_length=50, help_text='Title here')
    description = models.TextField(help_text='Descripton here')
    date_posted = models.DateField(auto_now_add=True)
    date_time_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['date_posted']