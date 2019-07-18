import graphene 
from graphene_django.types import DjangoObjectType

from .models import Programmer, Tag
from .models import Query as query_model


class ProgrammerType(DjangoObjectType):
    class Meta:
        model = Programmer 

class QueryType(DjangoObjectType):
    class Meta:
        model = query_model 

class TagType(DjangoObjectType):
    class Meta:
        model = Tag 

class Query(graphene.ObjectType):
    all_programmers = graphene.List(ProgrammerType)
    def resolve_all_programmers(self, info, **kwargs):
        return Programmer.objects.all()

    all_queries = graphene.List(QueryType)
    def resolve_all_queries(self, info, **kwargs):
        return query_model.objects.all()

    all_tags = graphene.List(TagType) 
    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

