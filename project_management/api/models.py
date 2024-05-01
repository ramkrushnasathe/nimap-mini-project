from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects_assigned')  # Custom related_name
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')

    def __str__(self):
        return self.project_name
