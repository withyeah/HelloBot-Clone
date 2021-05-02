from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import ScenarioViewSet, TarotViewSet

router = DefaultRouter()
router.register(r"scenarios", ScenarioViewSet)
router.register(r"tarots", TarotViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="HelloBot Clone API",
        default_version="v1",
        description="HelloBot LaMama Clone API",
        terms_of_service="https://github.com/withyeah",
        contact=openapi.Contact(email="yerang.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
]
