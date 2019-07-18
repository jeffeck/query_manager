from django.urls import include, path

from api import urls as api_urls
from . import views

urlpatterns = [
    path('', views.QueryList.as_view(), name='index'),
    path('test/', views.index),

    path('queries/', views.QueryList.as_view(), name='querylist'),
    path('queries/<int:pk>/', views.QueryDetail.as_view(), name='query_detail'),

    path('programmers/', views.ProgrammerList.as_view(), name='programmer_list'),
    path('programmers/<int:pk>/', views.ProgrammerDetail.as_view(), name='programmer_detail'),

    path('tags/', views.TagList.as_view(), name="tag_list"),

    path('api/', include(api_urls), name='api')
]
