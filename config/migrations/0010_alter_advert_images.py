# Generated by Django 5.0.6 on 2024-07-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0009_alter_advert_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Изображения'),
        ),
    ]
