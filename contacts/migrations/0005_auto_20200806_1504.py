# Generated by Django 3.0.8 on 2020-08-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20200806_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='facebook_page',
            field=models.CharField(max_length=200),
        ),
    ]
