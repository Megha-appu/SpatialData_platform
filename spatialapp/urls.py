from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, DensityViewSet

# Setting router for API
router = DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'density', DensityViewSet)

urlpatterns = [

    path('api/',include(router.urls)), # rediresting API urls
]