# Generated by Django 4.2 on 2023-06-07 12:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_articles_alter_productreview_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='productspicture',
            name='pictures',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='productspicture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='productspicture',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]
