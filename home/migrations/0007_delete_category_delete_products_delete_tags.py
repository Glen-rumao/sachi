# Generated by Django 4.1.2 on 2024-06-17 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_category_products_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]