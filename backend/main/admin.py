from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def published(self, obj):
        if obj.date <= timezone.now():
            return True
        return False
    published.boolean = True
    published.short_description = 'Опубліковано'

    list_display = ('title', 'published', 'date',)
    list_filter = ('date',)


@admin.register(StudentVideo)
class StudentVideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
