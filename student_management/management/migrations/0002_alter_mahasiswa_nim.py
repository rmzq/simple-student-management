# Generated by Django 3.2.6 on 2021-08-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='nim',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
