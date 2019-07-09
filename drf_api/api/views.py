from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, viewsets

from .serializers import QuerySerializer, ProgrammerSerializer, TagSerializer
from querymanager.models import Query, Programmer, Tag

# DRF Permissions:
    # AllowAny
    # IsAuthenticated
    # IsAdminUser
    # IsAuthenticatedOrReadOnly
    # DjangoModelPermissions
    # DjangoModelPermissionOrAnonReadOnly
    # DjangoObjectPermissions
    # Custom by overriding BasePermission

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = (permissions.IsAuthenticated,)

class ProgrammerViewSet(viewsets.ModelViewSet): 
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def index(request): 
    return HttpResponse("<h1>API Index Page</h1>")

    