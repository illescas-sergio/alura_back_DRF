# Generated by Django 5.0.1 on 2024-02-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]