# Generated by Django 4.2.5 on 2024-04-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='timeduration',
            field=models.IntegerField(null=True),
        ),
    ]