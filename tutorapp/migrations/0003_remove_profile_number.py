# Generated by Django 3.0.6 on 2020-06-10 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='number',
        ),
    ]