# Generated by Django 5.0.6 on 2024-07-08 21:28

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_alter_dateadvert_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='config.category', verbose_name='Родитель'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=10000, verbose_name='Объявление')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('rating', models.SmallIntegerField(default=0, verbose_name='Комментарий')),
                ('commentAdvert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.advert')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
