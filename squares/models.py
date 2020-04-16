from django.db import models

class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Square(models.Model):
    title = models.CharField('Название', max_length=50)
    year = models.PositiveSmallIntegerField('Год создания', default=2020)
    description = models.TextField('Описание')
    actual_version = models.IntegerField('Актуальная версия')
    image = models.ImageField('Изображение', upload_to='squares/')
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Квадрат'
        verbose_name_plural = 'Квадраты'
