# Generated by Django 4.0.5 on 2022-06-06 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_rename_posts_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
    ]
