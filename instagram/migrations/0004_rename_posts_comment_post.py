# Generated by Django 4.0.5 on 2022-06-06 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_rename_post_comment_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
    ]
