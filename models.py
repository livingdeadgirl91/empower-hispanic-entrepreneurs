from django.db import models
from django.contrib.auth.models import User

class Entrepreneur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=50)

    def __str__(self):
        return self.business_name
