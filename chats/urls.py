from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScenarioViewSet, TarotViewSet

router = DefaultRouter()
router.register(r'scenarios', ScenarioViewSet)
router.register(r'tarots', TarotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
