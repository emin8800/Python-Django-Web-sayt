# Generated by Django 5.0.1 on 2024-01-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_product_edu_alter_edu_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='edu'),
        ),
    ]
