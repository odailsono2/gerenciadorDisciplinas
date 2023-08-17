# Generated by Django 4.2.4 on 2023-08-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeArea', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='nomeCurso',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nomeProfessor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='turma',
            name='codigo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.area'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.area'),
        ),
    ]
