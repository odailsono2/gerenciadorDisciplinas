from enum import Enum
from openpyxl import load_workbook



class Area:

    nome:str

    cargaHoraria:float

    def __init__(self,nome):
        self.nome
    
    def __str__(self) -> str:
        return self.nome
    
    def setNome(self,nome):
        self.nome = nome

    def setCargaHoraria(self,cargaHoraria):
        self.cargaHoraria = cargaHoraria


class TiposDisciplina(Enum):
    REG = "REGULAR"

    OPT = "OPTATIVA"

class Disciplina:

    nome:str

    cargaHoraria:int

    nomeCurso:str

    periodo:int

    tipoDisciplina:str

    nomeArea:str

    professor:str

    def __init__(self,nome,periodo,cargaHoraria,nomeCurso,tipoDisciplina,nomeArea, professor):
        self.nome = nome
        self.periodo = periodo
        self.cargaHoraria = cargaHoraria
        self.nomeCurso = nomeCurso
        self.tipoDisciplina = tipoDisciplina
        self.nomeArea = nomeArea
        self.professor = professor
    
    def __str__(self):
        return vars(self)


class Professor:
    nome:str
    formacao:str
    disciplinas= []
    chTotal=0
    def __init__(self, nome,formacao, disciplina):
        self.nome = nome
        self.formacao = formacao
        self.disciplinas.append(disciplina)

    def __str__(self):
        return vars(self)
    
class Curso:
    nome:str
    disciplinas=[]
    duracaoSemestres:int = 0
    qtdDisciplinasRegulares: int = 0
    qtdDisciplinasOPT: int = 0
    chTotalDisciplinas = 0
    vetorCHsemestre = []
    vetorAreasDisciplinas = []
    vetorProfessores = []

    def __init__(self,nome, planilha):
        self.nome = nome

        self.conv_plan(planilha)

    def setDisciplinas(self,disciplinas):
        self.disciplinas = disciplinas
            
    def setDuracao(self,duracaoSemestres):
        self.duracaoSemestres = duracaoSemestres

    def setvetorChSemestre(self,vetorCHsemestre):
        if self.duracaoSemestres == len(vetorCHsemestre):
            self.vetorCHsemestre = vetorCHsemestre
        else:
            print("Numero de semestres deve ser igual a ", self.duracaoSemestres)
            print("Tamanh do vetor informado: ", len(vetorCHsemestre))
            return
    
    def calculaCHsemestre(self):

        
        for periodo in range(self.duracaoSemestres):

            ch = 0

            for disc in self.disciplinas:
            
                if disc.tipoDisciplina != "Regular":
                    continue
            
                if disc.periodo == periodo:
                    ch = ch + disc.cargaHoraria
            
            self.vetorCHsemestre.append(ch)



    def listarDisciplinas(self):
        for disc in self.disciplinas:
            
            membros=disc.__str__()
            print("\n-------------------------------")
            for atributo, valor in membros.items():
                print(atributo, " - " ,  valor )

    def listarProfessores(self):
        for prof in self.vetorProfessores:
            
            membros=prof.__str__()
            print("\n-------------------------------")
            for atributo, valor in membros.items():
                print(atributo, " - " ,  valor )

    def conv_plan(self,planilha):
        

        for (colA, colB, colC, colD, colE, colF, colG, colH, colI) in zip( planilha['A'],planilha['B'],planilha['C'],planilha['D'],planilha['E'],planilha['F'],planilha['G'], planilha['H'], planilha['I']):
            
            nomeCurso = colG.value
            
            if nomeCurso != self.nome:
                continue
            
            nomeDisciplina = colB.value.split('-')[1]
            

            if colA.value.isdigit():
                #print(colB.value)

                periodo = int (colA.value)

                if periodo > self.duracaoSemestres:
                    self.duracaoSemestres = periodo
               
                self.qtdDisciplinasRegulares = self.qtdDisciplinasRegulares + 1
            else:
                #print(colD.value)
                periodo = 0
               
                self.qtdDisciplinasOPT = self.qtdDisciplinasOPT + 1

            if colE.value.isdigit():
                cargaHoraria = int (colE.value)

            else:
                cargaHoraria = 0

            tipoDisciplina = colC.value


            nomeArea = colF.value

            professor = colH.value
            nomeFormacao =colI.value
                    
            tmpDisciplina = Disciplina(nomeDisciplina,
                                            periodo,
                                            cargaHoraria, 
                                            nomeCurso,
                                            tipoDisciplina,
                                            nomeArea, professor)

            self.disciplinas.append (tmpDisciplina)

            if professor != None:
                tmpProfessor = Professor(professor,nomeFormacao,tmpDisciplina)
                if tmpProfessor not in self.vetorProfessores:
                    self.vetorProfessores.append(tmpProfessor)


class Turmas:
    """
    Descreve uma turma
    """
    nome:str
    curso:Curso
    anoEntrada:int
    semestreEntrada:int
    qtdAlunos:int
    

    def __init__(self, nome:str,anoEntrada:int,semestreEntrada:int, duracaoSemestres:int):
        """
        Inicializa a classe turma
        """
        self.setNome(nome)

        self.setAnoEntrada(anoEntrada)

        self.semestreEntrada(semestreEntrada)

    
    def setCurso(self,curso):
        self.curso = curso

    def setqtdAlunos(self,qtdAlunos):
        self.qtdAlunos = qtdAlunos

    def setAnoEntrada(self,anoEntrada):
        self.anoEntrada = anoEntrada

    def setsemEntrada(self,semestreEntrada):
        self.semestreEntrada = semestreEntrada
    
    

class projecaoCH:
    ch:float
    periodo:int


        

wb = load_workbook(filename = '../files/grade.xlsx')

#ler disicplinas de um arquivo xlsx

planilha = wb['Planilha1']   # ler aba Planilha1 do arquivo xlsx

curso1 = Curso("CST Energias Renovaveis",planilha)