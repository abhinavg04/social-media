# Generated by Django 5.0.3 on 2024-03-17 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_post_user_post_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]
