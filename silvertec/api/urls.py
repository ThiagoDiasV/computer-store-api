from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


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
router.register(r"processors", views.ProcessorViewSet)
router.register(r"motherboards", views.MotherBoardViewSet)
router.register(r"memories", views.MemoryViewSet)
router.register(r"graphiccards", views.GraphicCardViewSet)
router.register(r"computers", views.ComputerViewSet)
router.register(r"orders", views.OrderViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
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
