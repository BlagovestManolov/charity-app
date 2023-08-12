# Generated by Django 4.2.3 on 2023-08-03 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_alter_projectimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='volunteers',
            field=models.ManyToManyField(related_name='project_volunteers', to=settings.AUTH_USER_MODEL),
        ),
    ]
