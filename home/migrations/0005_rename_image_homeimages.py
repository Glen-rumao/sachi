# Generated by Django 4.1.2 on 2024-06-17 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_image_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='HomeImages',
        ),
    ]