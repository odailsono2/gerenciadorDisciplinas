# Generated by Django 4.2.4 on 2023-08-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.CharField(max_length=50),
        ),
    ]
