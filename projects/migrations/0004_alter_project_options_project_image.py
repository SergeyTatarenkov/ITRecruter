# Generated by Django 4.1.3 on 2022-12-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_options_rename_tag_project_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='projects/default.jpg', null=True, upload_to='project'),
        ),
    ]
