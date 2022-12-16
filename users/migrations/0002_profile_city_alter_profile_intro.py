# Generated by Django 4.1.3 on 2022-12-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='intro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Основная специальность'),
        ),
    ]
