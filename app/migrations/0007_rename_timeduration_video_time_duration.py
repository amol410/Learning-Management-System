# Generated by Django 4.2.5 on 2024-04-07 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_video_timeduration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='timeduration',
            new_name='time_duration',
        ),
    ]