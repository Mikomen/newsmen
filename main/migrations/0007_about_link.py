# Generated by Django 3.2 on 2021-06-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='link',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
