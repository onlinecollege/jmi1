# Generated by Django 3.2.5 on 2021-08-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0018_auto_20210827_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='date',
        ),
        migrations.RemoveField(
            model_name='note',
            name='name',
        ),
        migrations.AddField(
            model_name='note',
            name='file_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='note',
            name='your_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='paper',
            name='category',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='paper',
            name='subject',
            field=models.CharField(default='', max_length=32),
        ),
    ]
