from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from django.utils import timezone


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
    serializer_class = PostSerializer
    pagination_class = None


class StudentVideoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StudentVideo.objects.filter(date__lte=timezone.now()).order_by('-date')
    serializer_class = StudentVideoSerializer
    pagination_class = None
