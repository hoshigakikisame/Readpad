# Generated by Django 3.1.5 on 2021-01-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='stok',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]
