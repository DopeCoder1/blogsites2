# Generated by Django 4.0.1 on 2022-01-31 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='дата изменение')),
                ('is_published', models.BooleanField(verbose_name='Опубликован ли?')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
        ),
    ]
