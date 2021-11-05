from django.urls import path
from .views import BoardPage

urlpatterns = [
    path('', BoardPage.as_view()),
]