from django.urls import path
from .views import Index, ThreadView

urlpatterns = [
    path('', Index.as_view()),
    path('thread/', ThreadView.as_view()),
]