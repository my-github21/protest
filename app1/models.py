from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
