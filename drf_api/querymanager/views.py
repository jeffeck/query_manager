from django.contrib.auth.mixins import LoginRequiredMixin
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
    # Need to bring in queries as well to be parsed on page
    # Overriding context object with function below
    # context_object_name = 'tags'
    template_name = 'tag_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_active'] = 'active'
        context['tags'] = Tag.objects.all()
        context['query_list'] = Query.objects.all()
        return context

class QueryList(LoginRequiredMixin, ListView): 
    # Login mixin requires a login url and redirect
    login_url = '/admin/'
    # redirect_field_name = 'redirect_to'

    model = Query 
    # ordering = ['id']
    # context_object_name = 'query_list'
    template_name = 'query_list.html'

    # class Meta:
    #     ordering = ['-id']

    # Overriding context_object_name
    def get_context_data(self, **kwargs):
        # Call the parent keyword arguments
        context = super().get_context_data(**kwargs)
        # This will be evaluated in nav.html to set active class
        context['query_active'] = 'active'
        # query_list.html template is expecting 'query_list' context
        context['query_list'] = Query.objects.all()
        return context


class QueryDetail(LoginRequiredMixin, DetailView): 
    login_url = '/admin/'

    model = Query 
    queryset = Query.objects.all()


class ProgrammerList(ListView):
    model = Programmer
    context_object_name = 'programmer_list'
    template_name = 'programmer_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programmer_active'] = 'active'
        context['query_list'] = Query.objects.all()
        context['programmer_list'] = Programmer.objects.all()
        return context 


class ProgrammerDetail(DetailView):
    model = Programmer
    queryset = Programmer.objects.all()
