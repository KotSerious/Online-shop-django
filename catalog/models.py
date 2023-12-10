from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(max_length=400, verbose_name="описание")
    image = models.ImageField(upload_to='product_image/', verbose_name="изображение", null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, verbose_name='категория', null=True, blank=True)
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
    description = models.CharField(max_length=400, verbose_name='описание', null=True, blank=True)

    # created_at = models.CharField(blank=True, max_length=150, null=True, verbose_name='наименование2')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
