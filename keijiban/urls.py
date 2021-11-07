from django.urls import path
from .views import Index, ThreadView, Create, CategoryView

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('threads/<pk>/', ThreadView.as_view(), name='thread'),
    path('create/', Create.as_view(), name='create'),
    path('category/<pk>/', CategoryView.as_view(), name='category'),
]