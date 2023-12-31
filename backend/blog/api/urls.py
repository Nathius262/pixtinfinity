from django.urls import path
from .views import PostViewSet,TagViewSet

app_name = 'blog'

urlpatterns = [
    path('post/<slug>/', PostViewSet.as_view(), name='detail_post_api'),
    path('post/', PostViewSet.as_view(), name='list_post_api'),
    path('tag/', TagViewSet.as_view(), name='list_tag_api'),
]