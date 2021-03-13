from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerialzer, GroupSerialzer
# Create your views here.
class UserViewsSet(viewsets.ModelViewSet):
    queryset =  User.objects.all().order_by('-date_joined')
    serializer_class =  UserSerialzer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerialzer
    permission_classes = [permissions.IsAuthenticated]