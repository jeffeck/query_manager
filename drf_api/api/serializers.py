from rest_framework import serializers

from querymanager.models import Query, Programmer, Tag

class TagSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Tag 
        fields = ('tag_name', 'tag_description')


class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query 
        fields = ('query_id', 'name', 'query', 'author', 'tags')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Programmer
        fields = ('programmer_id', 'name', 'title', 'hire_date')
