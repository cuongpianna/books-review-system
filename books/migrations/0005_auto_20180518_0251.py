# Generated by Django 2.0.5 on 2018-05-18 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='books.Book'),
        ),
        migrations.AlterField(
            model_name='status',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
