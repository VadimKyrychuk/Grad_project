from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

current_user = get_user_model()


class Category(models.Model):
    name_category = models.CharField(max_length=255, verbose_name='Название катеории')
    slug_category = models.SlugField(unique=True)

    def __str__(self):
        return self.name_category


class Product(models.Model):

    class Meta:
        abstract = True #


    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name_product = models.CharField(max_length=255, verbose_name='Название товара')
    slug_product = models.SlugField(unique=True)
    image_product = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.category} {self.name_product} {self.price}'


class BasketProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    basket = models.ForeignKey('Basket', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_basket')
    content = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    cont_object = GenericForeignKey('content', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Общая сумма')

    def __str__(self):
        return f'Товар: {self.product.name_product} {self.product.price}'


class Basket(models.Model):
    holder = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(BasketProduct, blank=True, related_name='related_basket')
    total_products = models.PositiveIntegerField(default=0)
    final_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Общая сумма')

    def __str__(self):
        return self.holder_id


class Customer(models.Model):
    user = models.ForeignKey(current_user, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    adress = models.CharField(max_length=255, verbose_name='Адресс проживания')


    def __str__(self):
        return f'Пользователь: {self.user.first_name} {self.user.last_name}'

