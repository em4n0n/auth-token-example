from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticaed
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer