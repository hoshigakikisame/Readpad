# Generated by Django 3.1.5 on 2021-01-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0006_pesanan_total_bayar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='bukti_tf',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]