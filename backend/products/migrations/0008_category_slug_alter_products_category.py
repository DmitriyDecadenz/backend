# Generated by Django 4.2 on 2023-06-08 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_category_sub_category_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_products', to='products.category', verbose_name='Категории'),
        ),
    ]
