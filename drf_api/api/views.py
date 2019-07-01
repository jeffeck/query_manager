from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import QuerySerializer, ProgrammerSerializer
from querymanager.models import Query, Programmer

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

class ProgrammerViewSet(viewsets.ModelViewSet): 
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

def index(request): 
    return HttpResponse("<h1>Index Page</h1>")

    