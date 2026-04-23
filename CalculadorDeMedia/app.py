alunos = [ # Lista que contém o nome e notas dos alunos
    {
    "Nome": "Victor",
    "Notas": {
        "Portugues": 10,
        "Matematica": 8,
        "Humanas": 9,
        "Ciencias": 9
        }
    },
    
    {"Nome": "Maria",
    "Notas": {
        "Portugues": 1,
        "Matematica": 2,
        "Humanas": 3,
        "Ciencias": 1
        }}
    
    
    ]

materias_peso = { # lista que armazena o peso das notas
        "Portugues": 4,
        "Matematica": 5,
        "Humanas": 3,
        "Ciencias": 5 }


def cadastro_alunos(): # Funcao que permite cadastrar mais alunos
    resposta = int(input("Quer adicionar mais alunos? Digite 1 para sim e 0 para não: "))
    
    if resposta > 0:
        nome = str(input("Nome do aluno: "))
        
        notas = {}
        notas["Portugues"] = float(input("Nota de Portugues: "))
        notas["Matematica"] = float(input("Nota de Matematica: "))
        notas["Humanas"] = float(input("Nota de Humanas: "))
        notas["Ciencias"] = float(input("Nota de Ciencias: "))
        
        aluno = { # cria um dicionário para o aluno cadastrado
            "Nome": nome,
            "Notas": notas
        }
        alunos.append(aluno) # insere o aluno cadastrado na lista de alunos
    else:
        return # caso o usuario digite 0 encerra a função
    cadastro_alunos() # reinicia a função
            
    
def calcular_media():
    media_aluno = {} # lista vazia, será preenchida em breve
    for aluno in alunos:
        soma = 0
        total_pesos = 0
        
        for materia, nota in aluno["Notas"].items():
            peso = materias_peso[materia]
            
            soma += nota * peso
            total_pesos += peso
        media = soma / total_pesos
        
        media_aluno[aluno["Nome"]] = round(media, 2) # preenche a lista com o nome do aluno e sua nota
    return media_aluno # encerra a função e retorna a lista


def situacao(aluno_media): # verifica o estado do aluno
    for aluno, media in aluno_media.items():
        estado = None
        if media < 5:
            estado = "Recuperação"
        elif media > 5:
            estado = "Aprovado"
        print(f"{aluno}: Situação: {estado}, média: {media}")

cadastro_alunos()
aluno_media = calcular_media()
situacao(aluno_media)
        
    
        
        
        
    