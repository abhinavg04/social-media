# Generated by Django 5.0.3 on 2024-03-19 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_post_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userpost', to='user.profile'),
        ),
    ]
