from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("processors/", views.ProcessorList.as_view()),
    path("processors/<int:pk>", views.ProcessorDetail.as_view()),
    path("motherboards/", views.MotherBoardList.as_view()),
    path("motherboards/<int:pk>", views.MotherBoardDetail.as_view()),
    path("memories/", views.MemoryList.as_view()),
    path("memories/<int:pk>", views.MemoryDetail.as_view()),
    path("graphiccards/", views.GraphicCardList.as_view()),
    path("graphiccards/<int:pk>", views.GraphicCardDetail.as_view()),
    path("computers/", views.ComputerList.as_view()),
    path("computers/<int:pk>", views.ComputerDetail.as_view()),
    path("orders/", views.OrderList.as_view()),
    path("orders/<int:pk>", views.OrderDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
