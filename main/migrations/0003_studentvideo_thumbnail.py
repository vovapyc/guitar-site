# Generated by Django 2.2.1 on 2019-05-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190512_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentvideo',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='', verbose_name='Прев`ю'),
            preserve_default=False,
        ),
    ]
