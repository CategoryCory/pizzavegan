# Generated by Django 3.0.8 on 2020-09-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200921_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=255),
        ),
    ]