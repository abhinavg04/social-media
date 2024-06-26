# Generated by Django 5.0.3 on 2024-03-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_remove_post_image_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='video'),
        ),
    ]
