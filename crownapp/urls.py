from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SchoolViewSet, FamilyViewSet

router = DefaultRouter()
router.register(r"schools", SchoolViewSet)
router.register(r"families", FamilyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
