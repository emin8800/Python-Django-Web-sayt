# Generated by Django 5.0.1 on 2024-01-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
