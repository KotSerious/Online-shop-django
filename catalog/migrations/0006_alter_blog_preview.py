# Generated by Django 4.2.3 on 2023-12-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/blog', verbose_name='Превью'),
        ),
    ]
