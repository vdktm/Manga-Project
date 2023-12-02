from django.urls import path
from .views import ComixListView, ComixDetailView, ComixFromCategory

urlpatterns = [
    path('', ComixListView.as_view(), name='home'),
    path('book/<str:slug>/', ComixDetailView.as_view(), name='book_detail'),
    path('category/<str:slug>/', ComixFromCategory.as_view(), name="book_by_category"),
]
