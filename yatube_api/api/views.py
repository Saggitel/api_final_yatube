from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Comment, Follow, Group, Post
from rest_framework import filters, status, viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs.get('post_id')
        )


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FollowViewSet(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
