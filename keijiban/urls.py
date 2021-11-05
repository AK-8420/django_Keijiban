from django.urls import path
from .views import BoardPage, Thread

urlpatterns = [
    path('', BoardPage.as_view()),
    path('thread/', Thread.as_view()),
]