from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)
    image = models.ImageField("Изображение", upload_to="category/", blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField('Название продукта', max_length=150)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField("Изображение", upload_to="product/", blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')


class Order(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='order_product')
    price = models.PositiveIntegerField('Цена')
    date = models.DateField('Дата покупки', auto_now=True)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('category')





