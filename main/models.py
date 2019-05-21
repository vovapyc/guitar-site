from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    title = models.CharField('Назва', max_length=100, unique=True)

    def count_of_posts(self):
        return Post.objects.filter(tags__in=[self]).count()

    def last_post(self):
        return Post.objects.filter(tags__in=[self]).last()

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        verbose_name = 'стаття'
        verbose_name_plural = 'статті'

    title = models.CharField('Назва', max_length=100)

    image = models.ImageField('Картинка', upload_to='images', help_text="Відношення сторін - 16:9")

    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    text = RichTextUploadingField('Текст')
    text_preview = models.TextField('Прев\'ю', help_text="До 450 символів", max_length=400)

    date = models.DateTimeField('Час публікації')

    def tags_str(self):
        return ','.join([t.title for t in Tag.objects.filter(post=self)])

    def publish(self):
        self.date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return "/news/post/%i/" % self.pk

    def __str__(self):
        return self.title


class StudentVideo(models.Model):
    class Meta:
        verbose_name = 'відео учня'
        verbose_name_plural = 'відео учнів'

    title = models.CharField('Назва', max_length=100)
    description = models.TextField('Опис')
    iframe = models.TextField('iFrame')
    thumbnail = models.ImageField('Прев`ю')
    date = models.DateTimeField('Час публікації')

    def __str__(self):
        return self.title
