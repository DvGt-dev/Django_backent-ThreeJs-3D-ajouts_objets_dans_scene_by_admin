from rest_framework.routers import DefaultRouter
from shapes.urls import shapes
from django.urls import path , include

# posts
router = DefaultRouter()
router.registry.extend(shapes.registry)
urlpatterns = [
    path('', include(router.urls)),
]