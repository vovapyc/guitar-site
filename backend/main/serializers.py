from .models import *
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


class PostSerializer(serializers.HyperlinkedModelSerializer):
    date_str = serializers.SerializerMethodField('date')

    def date(self, obj):
        return naturaltime(obj.date)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'image', 'text', 'text_preview', 'date', 'date_str',)


class StudentVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentVideo
        fields = ('pk', 'title', 'description', 'iframe')
