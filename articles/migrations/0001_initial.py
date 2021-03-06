# Generated by Django 3.0.8 on 2020-09-21 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('body', models.TextField()),
                ('featured_image', models.ImageField(blank=True, upload_to='images/')),
                ('featured_image_caption', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
