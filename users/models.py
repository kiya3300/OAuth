
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('agent', 'Agent'),
        ('player', 'Player'),
    )
    role = models.CharField(max_length=10, choices=ROLES)

