from django.conf import settings
from django.db import models

class Area(models.Model):
    nome =  models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    NumPeriodos = models.PositiveSmallIntegerField()
        
    def __str__(self) -> str:
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length = 50)
    periodo = models.PositiveSmallIntegerField()
    cargaHoraria = models.IntegerField()
    curso = models.CharField(max_length = 50)
    area = models.ForeignKey(Area, on_delete = models.DO_NOTHING)
    tipo = models.CharField(max_length=50, default="Regular")

    def __str__(self) -> str:
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete = models.DO_NOTHING)

    MinistraDisciplinas = models.ManyToManyField(Disciplina)
    
    def __str__(self) -> str:
        return self.nome


class Turma(models.Model):
    curso = models.CharField(max_length=50)
    anoEntrada = models.IntegerField()
    SemestresNum = models.PositiveSmallIntegerField(default = 8)

    def __str__(self) -> str:
        return self.codigo



