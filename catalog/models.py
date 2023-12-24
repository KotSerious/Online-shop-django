from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(max_length=400, verbose_name="описание")
    image = models.ImageField(upload_to='catalog/product_image/', verbose_name="изображение", **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, verbose_name='категория', **NULLABLE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена за покупку')
    date_of_add = models.DateField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    last_modified = models.DateField(auto_now=True, auto_now_add=False, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.product_name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('product_name',)


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='категория')
    description = models.CharField(max_length=400, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='catalog/blog', **NULLABLE, verbose_name='Превью')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'Блог: {self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title',)
