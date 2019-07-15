from django.shortcuts import render
from rest_framework import viewsets
from .models import open_account
from .serializers import accountserializer
# Create your views here.
#class accountview(viewsets.ModelViewSet):
#	quertset = Language.objects.all()
#	serializer_class = accountserializer
