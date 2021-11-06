from django.urls import path
from .views import Index, ThreadView

urlpatterns = [
    path('', Index.as_view()),
    path('threads/<pk>/', ThreadView.as_view()),
]