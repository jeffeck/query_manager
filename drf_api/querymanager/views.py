from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Programmer, Query

def index(request):
    return HttpResponse("<h1>Index page</h1>")


class QueryList(ListView): 
    print('in Query List')
    model = Query 
    print('model: ', model)
    context_object_name = 'query_list'
    print('context: ', context_object_name)    
    template_name = 'query_list.html'
    print('template: ', template_name)


class QueryDetail(DetailView): 
    model = Query 
    queryset = Query.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context 

