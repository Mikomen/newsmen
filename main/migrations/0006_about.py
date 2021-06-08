# Generated by Django 3.2 on 2021-06-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_is_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('text', models.TextField(default='')),
                ('achivment', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='upload')),
            ],
        ),
    ]