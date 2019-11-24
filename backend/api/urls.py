from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView


schema_view = get_schema_view(
    openapi.Info(
        title="Silvertec Rest API",
        default_version="1.0",
        description="Rest API for Silvertec Computer Store",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r"processors", views.ProcessorViewSet, base_name="processors")
router.register(
    r"motherboards", views.MotherBoardViewSet, base_name="motherboards"
)
router.register(r"memories", views.MemoryViewSet, base_name="memories")
router.register(
    r"graphiccards", views.GraphicCardViewSet, base_name="graphiccards"
)
router.register(r"computers", views.ComputerViewSet, base_name="computers")
router.register(r"orders", views.OrderViewSet, base_name="orders")
router.register(r"users", views.UserViewSet, base_name="users")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "openapi/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "openapi/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
