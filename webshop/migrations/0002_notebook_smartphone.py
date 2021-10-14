# Generated by Django 3.2.8 on 2021-10-14 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255, verbose_name='Название товара')),
                ('slug_product', models.SlugField(unique=True)),
                ('image_product', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('brand', models.CharField(max_length=64, verbose_name='Бренд смартфона')),
                ('model_smart', models.CharField(max_length=64, verbose_name='Модель смартфона')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('accum', models.CharField(max_length=255, verbose_name='Объем аккумулятора')),
                ('ram', models.CharField(max_length=64, verbose_name='Оперативная память')),
                ('sd_card', models.BooleanField(default=True, verbose_name='Возможность использования SD карты')),
                ('sd_card_max_size', models.CharField(max_length=255, verbose_name=' Максимальный объем карты памяти')),
                ('main_cam', models.CharField(max_length=64, verbose_name='Главная камера')),
                ('front_cam', models.CharField(max_length=64, verbose_name='Фронтальная камера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webshop.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255, verbose_name='Название товара')),
                ('slug_product', models.SlugField(unique=True)),
                ('image_product', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд ноутбука')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('cpu', models.CharField(max_length=255, verbose_name='Процессор')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('video', models.CharField(max_length=255, verbose_name='Видеокарта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webshop.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]