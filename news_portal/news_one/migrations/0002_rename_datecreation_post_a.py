# Generated by Django 4.1.2 on 2022-10-24 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_one', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dateCreation',
            new_name='a',
        ),
    ]
