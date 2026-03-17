def pegar_informacoes():
    # Cuida de erros e pega o valor inicial das variáveis.  
    try:
        nome = input("Qual é o nome do aparelho? ")
        potencia = float(input("Qual é a potência do aparelho em watts? "))
        tempo_de_uso = float(input("Qual é o tempo de uso? "))
    except ValueError:
        print("Erro: Você deve inserir um valor numérico!")
        pegar_informacoes()
        return
    
pegar_informacoes()
    