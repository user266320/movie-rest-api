# Generated by Django 5.0.4 on 2024-05-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='img',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='movies',
            name='summary',
            field=models.TextField(),
        ),
    ]
