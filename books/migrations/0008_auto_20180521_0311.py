# Generated by Django 2.0.5 on 2018-05-21 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180518_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='books.Book'),
        ),
    ]
