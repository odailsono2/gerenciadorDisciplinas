from django.conf import settings
from django.db import models

class Area(models.Model):
    nomeArea =  models.CharField(max_length=50)

class Curso(models.Model):
    nomeCurso = models.CharField(max_length=50)
    NumPeriodos = models.PositiveSmallIntegerField()
        
    def __str__(self) -> str:
        return self.nomeCurso

class Disciplina(models.Model):
    nomeDisciplina = models.CharField(max_length = 50)
    periodoDisciplina = models.PositiveSmallIntegerField()
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.nomeDisciplina


class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)

    #MinistraDisciplinas = models.Lista
    
    def __str__(self) -> str:
        return self.nomeProfessor


class Turma(models.Model):
    codigo = models.CharField(max_length=50)
    anoEntrada = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.codigo



