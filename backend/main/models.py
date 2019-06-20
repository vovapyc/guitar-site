from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    class Meta:
        verbose_name = 'акорд'
        verbose_name_plural = 'акорди'

    title = models.CharField('Назва', max_length=100)

    image = models.ImageField('Картинка', upload_to='images', help_text="Відношення сторін - 16:9")

    text = RichTextUploadingField('Текст')
    text_preview = models.TextField('Прев\'ю', help_text="До 450 символів", max_length=400)

    date = models.DateTimeField('Час публікації')

    def publish(self):
        self.date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return "/news/post/%i/" % self.pk

    def __str__(self):
        return self.title


class StudentVideo(models.Model):
    class Meta:
        verbose_name = 'відео урок'
        verbose_name_plural = 'відео уроки'

    title = models.CharField('Назва', max_length=100)
    description = models.TextField('Опис')
    iframe = models.TextField('Vimeo id')
    thumbnail = models.ImageField('Прев`ю')
    date = models.DateTimeField('Час публікації')

    def __str__(self):
        return self.title
