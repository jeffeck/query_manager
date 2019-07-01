from django.urls import include, path
from rest_framework import routers
from api import views 

router = routers.DefaultRouter()
router.register('query', views.QueryViewSet) 
router.register('programmer', views.ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
