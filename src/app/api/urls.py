from django.urls import path
from .views import ReadingListAPIView, ReadingDetailAPIView

urlpatterns = [

    path("", ReadingListAPIView.as_view()),
    path("<int:pk>/", ReadingDetailAPIView.as_view()),
]
