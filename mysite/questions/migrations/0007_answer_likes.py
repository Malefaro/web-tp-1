# Generated by Django 2.0.2 on 2018-04-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
    ]