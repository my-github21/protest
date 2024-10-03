
from rest_framework import viewsets, permissions
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
import requests
from django.shortcuts import render
from django.http import HttpResponse

def get_clients(request):
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNjIzNTk5LCJpYXQiOjE3MjM2MjMyOTksImp0aSI6ImIzN2QzZTgwZTg1MjRiZTJiZDRiNTczN2IyNWYxNDMwIiwidXNlcl9pZCI6Mn0.Pc8TiQt3QUS-reb09t_9MnJ1XFlFhYWhhGY_INkJJAc'  # Replace with the actual token
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get('http://127.0.0.1:8000/api/clients/', headers=headers)

    return HttpResponse(response.content)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require login

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require login


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     # No need for permission_classes; it defaults to AllowAny

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     # No need for permission_classes; it defaults to AllowAny