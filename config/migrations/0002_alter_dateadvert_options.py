# Generated by Django 5.0.6 on 2024-07-03 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dateadvert',
            options={'ordering': ['id'], 'verbose_name': 'Срок', 'verbose_name_plural': 'Сроки'},
        ),
    ]
