from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def published(self, obj):
        if obj.date <= timezone.now():
            return True
        return False
    published.boolean = True
    published.short_description = 'Опубліковано'

    list_display = ('title', 'published', 'date',)
    list_filter = ('tags', 'date')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    def count_of_posts(self, obj):
        return obj.count_of_posts()
    count_of_posts.short_description = 'Кількість постів'

    def last_post_title(self, obj):
        last_post = obj.last_post()
        return format_html('<a href="/admin/news/post/{}">'
                           '{} ({})</a>'.format(last_post.pk, last_post.title, last_post.date))
    last_post_title.short_description = 'Останній пост'

    def all_tag_posts(self, obj):
        return format_html('<a href="/admin/news/post/?tags__id__exact={}">Переглянути</a>'.format(obj.pk))
    all_tag_posts.short_description = 'Всі пости за тегом'

    list_display = ('title', 'count_of_posts', 'last_post_title')
    readonly_fields = ('count_of_posts', 'last_post_title', 'all_tag_posts')


@admin.register(StudentVideo)
class StudentVideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
