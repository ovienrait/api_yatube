from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .mixins import AuthorPermissionsMixin


class PostViewSet(AuthorPermissionsMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(AuthorPermissionsMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(
                Post,
                id=self.kwargs.get('post_id')
            )
        )

    def get_queryset(self):
        return Comment.objects.filter(
            post=Post.objects.get(id=self.kwargs.get('post_id'))
        )
