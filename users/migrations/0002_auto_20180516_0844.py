# Generated by Django 2.0.5 on 2018-05-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/user/%Y/%m/%d'),
        ),
    ]
