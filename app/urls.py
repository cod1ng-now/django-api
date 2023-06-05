from django.urls import path
from .views import  PostListView, PostDetailView, CreateView, update, delete
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', update.as_view(), name='update'),
    path('create/', CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', delete.as_view(), name='delete'),
]