# Generated by Django 4.2.3 on 2023-12-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/product_image/', verbose_name='изображение'),
        ),
    ]