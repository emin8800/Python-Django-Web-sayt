# Generated by Django 5.0.1 on 2024-01-25 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]