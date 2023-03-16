from django.db import models
from django.utils import timezone

class URL(models.Model):
    url = models.CharField(max_length=250)
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    custom_name = models.CharField(max_length=10, null=True, blank=True)
    counter = models.IntegerField(default=0)
