# Generated by Django 4.2.1 on 2023-06-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postAuthor',
            new_name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]
