# Generated by Django 3.2.6 on 2021-08-07 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=32)),
                ('jurusan', models.CharField(choices=[('IF', 'INFORMATIKA'), ('TI', 'TEKNIK INDUSTRI'), ('TE', 'TEKNIK ELEKTRO'), ('TM', 'TEKNIK MESIN'), ('TK', 'TEKNIK KIMIA')], default='IF', max_length=2)),
            ],
        ),
    ]