# Generated by Django 4.1.3 on 2022-12-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_options_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='projects/default.jpg', null=True, upload_to='projects'),
        ),
    ]
