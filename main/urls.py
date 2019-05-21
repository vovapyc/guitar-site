from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'student-videos', views.StudentVideoViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='index'),
    path('students_videos/', TemplateView.as_view(template_name='main/students_videos.html'), name='students_videos'),
    path('video/', TemplateView.as_view(template_name='main/video_detailed.html'), name='video_detailed'),
    path('news/', TemplateView.as_view(template_name='main/news.html'), name='news'),
    path('post/', TemplateView.as_view(template_name='main/post.html'), name='post'),
    path('contacts/', TemplateView.as_view(template_name='main/contacts.html'), name='contacts'),
    path('api/', include(router.urls)),
]
