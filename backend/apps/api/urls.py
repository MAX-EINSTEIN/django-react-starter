from django.urls import path
from django.views.generic import TemplateView
from .views import PostsListView, PostDetailView

app_name = 'api'

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts_crud_page'),
    path('posts/', PostsListView.as_view(), name='posts_list')
]
