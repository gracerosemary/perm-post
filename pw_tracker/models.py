from django.db import models
from django.contrib.auth import get_user_model

class Tracker(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website
