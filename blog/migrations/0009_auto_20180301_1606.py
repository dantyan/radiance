# Generated by Django 2.0.2 on 2018-03-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180228_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='article',
            name='count_comments',
            field=models.BigIntegerField(default=0, verbose_name='Count comments'),
        ),
    ]
