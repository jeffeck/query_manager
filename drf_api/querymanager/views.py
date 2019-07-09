from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from django.forms.models import model_to_dict

from .models import Programmer, Query, Tag

def index(request):
    return HttpResponse("<h1>Index page</h1>")


class TagList(ListView):
    model = Tag 
    context_object_name = 'tags'
    template_name = 'tag_list.html'


class QueryList(ListView): 
    model = Query 
    ordering = ['-query_id']
    # context_object_name = 'query_list'
    template_name = 'query_list.html'

    # Overriding context_object_name
    def get_context_data(self, **kwargs):
        # Call the parent keyword arguments
        context = super().get_context_data(**kwargs)

        # This will be evaluated in nav.html to set active class
        context['query_active'] = 'active'
 
        # query_list.html template is expecting 'query_list' context
        context['query_list'] = Query.objects.all()
        return context


class QueryDetail(DetailView): 
    model = Query 
    queryset = Query.objects.all()


class ProgrammerList(ListView):
    model = Programmer
    context_object_name = 'programmer_list'
    template_name = 'programmer_list.html'


class ProgrammerDetail(DetailView):
    model = Programmer
    queryset = Programmer.objects.all()
