from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """
    Модель для продуктов
    """
    product_name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(max_length=400, verbose_name="описание")
    image = models.ImageField(upload_to='catalog/product_image/', verbose_name="изображение", **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, verbose_name='категория', **NULLABLE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена за покупку')
    date_of_add = models.DateField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    last_modified = models.DateField(auto_now=True, auto_now_add=False, verbose_name='дата изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Продавец')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.product_name} {self.price} {self.category}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('product_name',)


        permissions = [
            (
                'set_is_published',
                'Can is_published'
            ),
            (
              'set_description',
              'Can description'
            ),
            (
                'set_category',
                'Can category'
            )
        ]


class Version(models.Model):
    """
    Модель для версии продукта
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.AutoField(primary_key=True, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Наименовании версии')
    is_valid = models.BooleanField(default=True, verbose_name='Признак версии')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'Версия: "{self.version_name}" ({self.version_number}) для продукта {self.product}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)


class Category(models.Model):
    """
    Модель для категории
    """
    category_name = models.CharField(max_length=150, verbose_name='категория')
    description = models.CharField(max_length=400, verbose_name='описание', **NULLABLE)

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.category_name}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):
    """
    Модель для блога
    """
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='catalog/blog', **NULLABLE, verbose_name='Превью')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'Блог: {self.title}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title',)
