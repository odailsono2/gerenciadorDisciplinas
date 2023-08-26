from django.shortcuts import render
from openpyxl import load_workbook
from .models import Disciplina, Area
from enum import Enum

class TiposDisciplina(Enum):
    REG = "REGULAR"

    OPT = "OPTATIVA"

class DisciplinaAux:

    nome:str

    cargaHoraria:int

    curso:str

    periodo:int

    tipoDisciplina:str

    area:str

    def __init__(self,nome,periodo,cargaHoraria,curso,tipoDisciplina,area):
        self.nome = nome
        self.periodo = periodo
        self.cargaHoraria = cargaHoraria
        self.curso = curso
        self.tipoDisciplina = tipoDisciplina
        self.area = area
    def __str__(self):
        return "%s, %d° periodo, %d h/a, %s" %(self.nome,self.periodo,self.cargaHoraria,self.tipoDisciplina)


class ProfessorAux:
    nome:str
    area:str
    disciplinas= []
    def __init__(self, nome,area):
        self.nome = nome
        self.area = area

class CursoAux:
    nome:str
    numPeriodo: int
    gradeDisciplinas: DisciplinaAux
    def __init__(self,nome,numPeriodo):
        self.nome = nome
        self.numPeriodo = numPeriodo

class TurmaAux:
    anoEntrada:str
    professores: ProfessorAux


#pega as celulas da coluna D: componente curricular
#coluna B: periodo
#coluna J: carga horária

def conv_plan(planilha)->DisciplinaAux:
    disciplinas = []

    for (colD,ColB, ColJ) in zip( planilha['D'],planilha['B'],planilha['J']):

        nome = colD.value.split('-')[1]

        if ColB.value.isdigit():
            #print(colB.value)
            periodo = int (ColB.value)
            tipoDisciplina = TiposDisciplina.REG.value

        else:
            #print(colD.value)
            periodo = 0
            tipoDisciplina = TiposDisciplina.OPT.value

        if ColJ.value.isdigit():
            cargaHoraria = int (ColJ.value)

        else:
            cargaHoraria = 0

        disciplinas.append ( DisciplinaAux(nome,
                                           periodo,
                                           cargaHoraria, 
                                           'CST Energias',
                                           tipoDisciplina,
                                           'Processos Industriais') )

    return disciplinas

def carrega_xls(request):
    #Carrega arquivo xlsx

    wb = load_workbook(filename = './files/grade.xlsx')

    #ler disicplinas de um arquivo xlsx

    planilha = wb['Planilha1']   # ler aba Planilha1 do arquivo xlsx

    listaDisciplinas = conv_plan(planilha)

    for tempDisc in listaDisciplinas:
        tempArea = Area.objects.create(nome = tempDisc.area)

        # Verificar se já existe um produto com o mesmo nome e preço
        disc_existente = Disciplina.objects.filter(nome=tempDisc.nome).exists()
        
        if disc_existente:
            continue

        bdDisciplina = Disciplina(nome = tempDisc.nome,
                                  periodo = tempDisc.periodo ,
                                  cargaHoraria = tempDisc.cargaHoraria,
                                  curso = tempDisc.curso ,
                                  area = tempArea,
                                  tipo = tempDisc.tipoDisciplina)
    
        bdDisciplina.save()

def ListarDisciplinasBD(request):
    
    listaDisciplinas = Disciplina.objects.all()

    return render(request, 'disciplinas/list_disciplinas.html', {'Disciplinas':listaDisciplinas})

