from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'processors', views.ProcessorViewSet)
router.register(r'motherboards', views.MotherBoardViewSet)
router.register(r'memories', views.MemoryViewSet)
router.register(r'graphiccards', views.GraphicCardViewSet)
router.register(r'computers', views.ComputerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
