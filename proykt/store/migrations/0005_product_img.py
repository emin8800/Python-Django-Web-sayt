# Generated by Django 5.0.1 on 2024-01-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
