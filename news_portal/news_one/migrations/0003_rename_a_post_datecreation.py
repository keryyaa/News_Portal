# Generated by Django 4.1.2 on 2022-10-24 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_one', '0002_rename_datecreation_post_a'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='a',
            new_name='dateCreation',
        ),
    ]