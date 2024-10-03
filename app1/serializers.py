from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Client
        fields = '__all__'
        
        
        
        
        

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = '__all__'

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']
