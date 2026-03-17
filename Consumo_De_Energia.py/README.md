# Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-EFBE08?style=for-the-badge&logo=lightning&logoColor=black)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-green?style=for-the-badge)

## Sobre o projeto

Este projeto e uma **calculadora de consumo de energia** feita em **Python**. Ela foi criada para receber dados de um aparelho eletrico, calcular o **consumo mensal em kWh** e mostrar o **preco estimado da conta de energia** com base no tempo de uso diario.

## Objetivo do sistema

O objetivo do sistema e ajudar o usuario a:

- Informar o nome do aparelho.
- Digitar a potencia em watts.
- Informar quantas horas por dia o aparelho fica ligado.
- Inserir o preco do kWh da cidade.
- Calcular automaticamente o consumo mensal e o custo estimado.

## Linguagem utilizada

- **Python**

## Formula utilizada

O calculo do consumo mensal segue esta formula:

```text
consumo = (potencia * horas_de_uso * 30) / 1000
valor = consumo * preco_do_kw
```

### Explicacao

- `potencia`: potencia do aparelho em watts.
- `horas_de_uso`: quantidade de horas por dia.
- `30`: estimativa de dias no mes.
- `/ 1000`: converte de Wh para kWh.
- `valor`: custo estimado com base no preco do kWh.

## Exemplo de saida

```text
Consumo: 150.0 kWh/mes, Preco estimado: R$105.00
```

## Como executar o programa

1. Tenha o **Python** instalado no computador.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo com o comando:

```bash
python app.py
```

4. Preencha os dados solicitados no terminal.

## Funcionalidades

- Validacao de entradas numericas.
- Tratamento de erros com repeticao do processo.
- Calculo do consumo mensal em kWh.
- Estimativa do valor mensal gasto com energia.

## Ideias futuras

- Adicionar interface grafica.
- Calcular consumo de varios aparelhos.
- Gerar relatorio mensal.

## Autor

Projeto desenvolvido para pratica de logica de programacao com Python. ⚡
