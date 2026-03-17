#Recebe os Valores digitados pelo usuário:
def pegar_dados():
    nome = str(input("Escreva seu nome: "))
    try:
        distancia = float(input(f"Seja bem vindo {nome}! Por favor insira a distância em KM: "))
        velocidade = float(input("Qual é a velocidade média do percurso?: "))
    except ValueError:
        print("Erro: Só são permitidos números. É necessário inserir um valor em números!")
        return pegar_dados()
    return nome, distancia, velocidade
    
#Calcula o tempo necessario para completar o percurso
def calcular(distancia, velocidade):
    tempoem_horas = distancia / velocidade
    tempoem_dias = tempoem_horas / 24
    return tempoem_horas, tempoem_dias

#Declara o valor das variaveis
nome, distancia, velocidade = pegar_dados()
tempoem_horas, tempoem_dias = calcular(distancia, velocidade)

#Escreve a saudação
print("Iniciando Simulação")
print(f"Com uma velociadade de {velocidade}km/h, sua viagem vai levar aproximadamente {tempoem_horas:.2f} horas.")
print(f"Em dias isso seria {tempoem_dias:.2f}")
print("Tenha uma boa viagem!!!")