from django.db import models
from django.utils.text import slugify

from mptt.models import MPTTModel, TreeForeignKey
from base.utils import translit_to_eng


class Category(MPTTModel):
    name = models.CharField('Название', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        """ Сортировка по вложенности """
        order_insertion_by = ('name',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)


class BrandModel(models.Model):
    name = models.CharField('Модель', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд', related_name='models')

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)


class Color(models.Model):
    name = models.CharField('Цвет', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)


class Size(models.Model):
    name = models.CharField('Размер', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)


class RAM(models.Model):
    name = models.CharField('ОЗУ', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)

    class Meta:
        verbose_name = 'ОЗУ'
        verbose_name_plural = 'ОЗУ'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)


class Memory(models.Model):
    name = models.CharField('Память', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='slug', blank=True)

    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(translit_to_eng(self.name))}'
        super().save(*args, **kwargs)
