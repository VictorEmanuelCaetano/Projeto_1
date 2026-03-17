def pegar_informacoes():
    # Cuida de erros e pega o valor inicial das variáveis.
    while True:
        nome = input("Qual é o nome do aparelho? ")
        try:
            potencia = float(input("Qual é a potência do aparelho em watts? "))
            horas_de_uso = float(input("Qual é o tempo de uso por dia em horas? "))
            preco_do_kw = float(input("Qual é o preço do kW da sua cidade? Obs: Se você não sabe apenas digite 0 para estimar uma média de preço: "))
        except ValueError:
            print("Erro: Você deve inserir um valor numérico!")
            continue
        if preco_do_kw == 0:
            preco_do_kw = 0.7
        
        if potencia <= 0:
            print("Erro: Potencia não pode ser menor que 1")
            continue
        
        if horas_de_uso <= 0 or horas_de_uso > 24:
            print("Erro: Tempo não pode ser menor que 1 ou maior que 24")
            continue
        
        if preco_do_kw <= 0:
            print("Erro: Preço não pode ser menor que 1")
            continue
        
        return nome, potencia, horas_de_uso, preco_do_kw

nome, potencia, horas_de_uso, preco_do_kw = pegar_informacoes()
#calcula o consumo e valor
def calcular(potencia, horas_de_uso, preco_do_kw):
    consumo = (potencia * horas_de_uso * 30) / 1000
    valor = consumo * preco_do_kw
    return consumo, valor

consumo, valor = calcular(potencia, horas_de_uso, preco_do_kw)
#escreve o resultado na tela
print(f"Aparelho: {nome}, Consumo: {consumo} kWh/mês, Preço estimado: R${valor:.2f} ")