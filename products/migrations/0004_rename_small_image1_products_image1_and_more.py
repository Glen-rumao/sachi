# Generated by Django 4.1.2 on 2024-06-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_image2_products_large_image1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='small_image1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='large_image1',
            new_name='large_image',
        ),
        migrations.AddField(
            model_name='products',
            name='small_image',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]
