from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'text', 'text_preview', 'date', 'tags_str')


class StudentVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentVideo
        fields = ('title', 'description', 'iframe')
