# Generated by Django 4.1.7 on 2023-04-25 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='desc1',
        ),
    ]
