# Generated by Django 3.0.5 on 2020-04-11 12:46

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Squares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='Год создания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('actual_version', models.IntegerField(verbose_name='Актуальная версия')),
                ('image', models.ImageField(upload_to='squares/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='squares.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Квадрат',
                'verbose_name_plural': 'Квадраты',
            },
        ),
    ]
