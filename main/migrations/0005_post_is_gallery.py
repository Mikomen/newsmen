# Generated by Django 3.2 on 2021-06-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_gallery',
            field=models.BooleanField(default=False),
        ),
    ]