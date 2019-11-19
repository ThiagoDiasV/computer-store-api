from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("processors/", views.ProcessorList.as_view()),
    path("processors/<int:pk>", views.ProcessorDetail.as_view()),
    path("motherboards/", views.MotherBoardList.as_view()),
    path("motherboards/<int:pk>", views.MotherBoardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
