# Generated by Django 3.2.5 on 2021-07-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0012_auto_20210716_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='moon',
        ),
        migrations.AlterField(
            model_name='paper',
            name='subject',
            field=models.CharField(choices=[('Islamiat I', 'Islamiat I'), ('English I', 'English I'), ('Animal Diversity I', 'Ad 1'), ('Plant Diversity I', 'Pd 1')], default='', max_length=32),
        ),
    ]