from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"board", views.BoardViewSet, basename="board")

urlpatterns = router.urls
