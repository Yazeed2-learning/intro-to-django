# Generated by Django 2.0.7 on 2021-03-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summery',
            field=models.TextField(blank=True),
        ),
    ]
