# Generated by Django 4.2 on 2024-06-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='pic.png', upload_to='profile_images'),
        ),
    ]
