from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('queries/', views.QueryList.as_view(), name='querylist'),
    # path('queries/', views.index, name='querylist'),
    path('queries/<int:pk>/', views.QueryDetail.as_view(), name='query_detail'),
]
