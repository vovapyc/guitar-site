# Generated by Django 2.2.2 on 2019-06-06 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190606_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentvideo',
            old_name='video_id',
            new_name='iframe',
        ),
    ]
