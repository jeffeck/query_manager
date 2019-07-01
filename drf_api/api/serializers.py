from rest_framework import serializers

from querymanager.models import Query, Programmer

class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query 
        fields = ('query_id', 'name', 'query', 'author')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Programmer
        fields = ('programmer_id', 'name')
