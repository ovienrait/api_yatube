from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]
