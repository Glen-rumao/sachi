# Generated by Django 4.1.2 on 2024-06-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_cate_products_desc_products_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image2',
            new_name='large_image1',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='image3',
            new_name='large_image2',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='image1',
            new_name='small_image1',
        ),
        migrations.AddField(
            model_name='products',
            name='large_image3',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='products',
            name='small_image2',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='products',
            name='small_image3',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]