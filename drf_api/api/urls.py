from django.urls import include, path
from rest_framework import routers
from api import views 

router = routers.DefaultRouter()
router.register('query', views.QueryViewSet) 
router.register('programmer', views.ProgrammerViewSet)
router.register('tag', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls), name="api"),
]
