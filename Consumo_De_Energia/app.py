import os
import time
from datetime import datetime
from pathlib import Path

DIAS_NO_MES = 30 #variáveis padrão que podem ser ajustadas conforme a necessidade
PREcO_DO_KW_PADRAO = 0.75

'''
Devido a algum bug do vs code, para a funcão de limpar funcionar corretamente execute o código no terminal dedicado
consertado! (talvez...)

'''
def limpar(): # verifica o sistema operacional do usuário, se é windows executa "cls", se é linux ou mac executa "clear"
    os.system("cls" if os.name == "nt" else "clear")
    
#entrada  
def pegar_informacoes():
    # cuida de erros e pega o valor inicial das variáveis.
    while True: # o loop while serve para não travar o código na hora de verificar erros
        limpar() # chama a funcão para limpar o output velho
        print("-" * 100) # estética
        
        print("calculadora de consumo elétrico \n")
        nome = input("Qual é o nome do aparelho?\n    ").strip() # Recebe o nome do aparelho
        print(" "* 100) # estética
        if not nome: # Se o nome estiver em branco, dá um erro e reinicia
            limpar()
            print("O nome não pode estar em branco!")
            continue
        
        try: # try, tenta receber os valores numéricos, se estiverem corretos ok! mas se estiverem errados chama except: linha 9
            potencia = float(input("Qual é a potência do aparelho em watts? \n    ")) # Recebe a potencia do aparelho
            print(" "* 100)
            
            horas_de_uso = float(input("Qual é o tempo de uso por dia em horas? \n    ")) # Recebe a o tempo de uso diário
            print(" "* 100)
            
            entrada_preco = input("Qual é o preco do kW da sua cidade? Obs: Se você não sabe apenas deixe em branco para estimar uma média de preco: \n    ").strip() # Preco do KiloWatt, se você inserir 0 coloca uma média aproximada para todo o Brasil
            print(" "* 100)
            entrada_preco = entrada_preco.replace(",", ".")
            if entrada_preco == "": #Se voce nao souber o preco do kW, recebe um enter vazio e muda o valor automaticamente
                preco_do_kw = PREcO_DO_KW_PADRAO
            else: # caso o preco do kw for inserido
                preco_do_kw = float(entrada_preco)
            
        except ValueError: # Prossegue se algum valor de cima estiver errado ^
        
            print("Erro: Você deve inserir um valor numérico!")
            time.sleep(3)
            limpar()
            continue # Para o código a partir desse ponto e reinicia o loop
              
        # os IFs seguintes fazem a mesma coisa, lidam com valores negativos, com execão do segundo que não permite que um dia tenha mais de 24 horas
        if potencia <= 0:
            
            print("Erro: Potencia não pode ser menor que 1")
            time.sleep(3)
            limpar()
            continue
        
        if horas_de_uso <= 0 or horas_de_uso > 24:
            
            print("Erro: Tempo não pode ser menor que 1 ou maior que 24")
            time.sleep(3)
            limpar()
            continue
        
        if preco_do_kw <= 0:
        
            print("Erro: Preco não pode ser menor que 1")
            time.sleep(3)
            limpar()
            continue
        
        # muito importante! como as variáveis só existem dentro dessa funcão, return faz o papel de declarar elas para que seja possível usa-las fora da funcão.
        return nome, potencia, horas_de_uso, preco_do_kw
    
    


# processamento
#calcula o consumo e valor
def calcular(potencia, horas_de_uso, preco_do_kw):
    consumo = (potencia * horas_de_uso * DIAS_NO_MES) / 1000 # fórmula do consumo
    valor = consumo * preco_do_kw # valor da conta
    
    return consumo, valor # retorna consumo e valor porque não existem fora da funcão


#saída
def main():
    nome, potencia, horas_de_uso, preco_do_kw = pegar_informacoes() 
    consumo, valor = calcular(potencia, horas_de_uso, preco_do_kw)

    #escreve o resultado na tela
    for i in range(3): # Um delay de 3 segundos usando o loop for para escrever na tela: calculando, adiciona um ponto final a cada segundo.
        limpar()
        print(f"calculando{'.'*i}")
        time.sleep(1)
        
    print(f"Aparelho: {nome} \nconsumo: {consumo:.2f} kWh/mês \nPreco estimado: R${valor:.2f}")
    pergunte_para_salvar(nome, consumo, valor)
    
    restart = input("Quer calcular outro aparelho? s/n? ").lower()
    if restart == "s":
        return main()
    else:
        return
    
    
        
def pergunte_para_salvar(nome, consumo, valor):
    confirmacão = input("Gostaria de salvar o resultado em um arquivo? s/n? ").lower()
    if confirmacão == "s":
        salvar_dados(nome, consumo, valor)
    else:
        return
    
    
def salvar_dados(nome, consumo, valor):
    pasta_do_código = Path(__file__).resolve().parent
    caminho_arquivo = pasta_do_código / "Dados Salvos.txt"
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
    
    texto = (
        f"Data: {data_formatada} \n"
        f"Aparelho: {nome} \n"
        f"consumo: {consumo:.2f} kWh/mês \n"
        f"Preco estimado: R${valor:.2f} \n \n \n \n"
        
    )
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    print("Informacões salvas com sucesso!")

    
if __name__ == "__main__":
    main()
