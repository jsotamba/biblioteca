from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, create_from_json

router = DefaultRouter()
router.register(r'libri', LibroViewSet, basename='libro-list-create')

urlpatterns = [
    path('', include(router.urls)),
    path('create-from-json/', create_from_json, name='create-from-json'),
]
