# Generated by Django 3.1.6 on 2021-02-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата покупки'),
        ),
    ]