# Generated by Django 5.0.1 on 2024-02-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]