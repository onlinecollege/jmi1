# Generated by Django 3.2.5 on 2021-09-17 09:07

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
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=32)),
                ('title', models.CharField(default='', max_length=64)),
                ('source', models.CharField(default='', max_length=164)),
                ('your_name', models.CharField(default='', max_length=64)),
                ('file_url', models.URLField(default='')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=32)),
                ('title', models.CharField(default='', max_length=64)),
                ('uploader', models.CharField(default='', max_length=64)),
                ('category', models.CharField(default='', max_length=12)),
                ('year', models.IntegerField(default=2021)),
                ('file_url', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
                ('content', models.TextField(default='', max_length=5000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
