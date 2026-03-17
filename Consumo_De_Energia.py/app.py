def pegar_informacoes():
    # Cuida de erros e pega o valor inicial das variáveis.
    while True: # o loop while serve para não travar o código na hora de verificar erros
        
        nome = input("Qual é o nome do aparelho? ") # Recebe o nome do aparelho
        
        try: # try, tenta receber os valores numéricos, se estiverem corretos ok! mas se estiverem errados chama except: linha 9
            potencia = float(input("Qual é a potência do aparelho em watts? ")) # Recebe a potencia do aparelho
            horas_de_uso = float(input("Qual é o tempo de uso por dia em horas? ")) # Recebe a o tempo de uso diário
            preco_do_kw = float(input("Qual é o preço do kW da sua cidade? Obs: Se você não sabe apenas digite 0 para estimar uma média de preço: ")) # Preço do KiloWatt, se você inserir 0 coloca uma média aproximada para todo o Brasil
            
        except ValueError: # Prossegue se algum valor de cima estiver errado ^
            print("Erro: Você deve inserir um valor numérico!")
            continue # Para o código a partir desse ponto e reinicia o loop
        
        if preco_do_kw == 0: # Se você não souber o preço do kw
            preco_do_kw = 0.7 
        
        # os IFs seguintes fazem a mesma coisa, lidam com valores negativos, com exeção do segundo (linha 24) que não permite que um dia tenha mais de 24 horas
        if potencia <= 0:
            print("Erro: Potencia não pode ser menor que 1")
            continue
        
        if horas_de_uso <= 0 or horas_de_uso > 24:
            print("Erro: Tempo não pode ser menor que 1 ou maior que 24")
            continue
        
        if preco_do_kw <= 0:
            print("Erro: Preço não pode ser menor que 1")
            continue
        
        # muito importante! como as variáveis só existem dentro dessa função, return faz o papel de declarar elas para que seja possível usa-las fora da função.
        return nome, potencia, horas_de_uso, preco_do_kw

nome, potencia, horas_de_uso, preco_do_kw = pegar_informacoes() # O valor das variáves corresponde ao return da linha 33
#calcula o consumo e valor
def calcular(potencia, horas_de_uso, preco_do_kw): # essa parte ficou um pouco confusa mas resumindo, usei parâmetros para evitar erros futuros caso eu adicione mais coisas a esse código.
    consumo = (potencia * horas_de_uso * 30) / 1000 # fórmula do consumo
    valor = consumo * preco_do_kw # valor da conta
    return consumo, valor # retorna consumo e valor porque não existem fora da função

consumo, valor = calcular(potencia, horas_de_uso, preco_do_kw) # traz as variáveis para fora da função

#escreve o resultado na tela
print(f"Aparelho: {nome}, Consumo: {consumo} kWh/mês, Preço estimado: R${valor:.2f} ")