# Generated by Django 5.0.6 on 2024-07-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_avatar_alter_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
        ),
    ]
