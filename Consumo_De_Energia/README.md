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

## No futuro
- Adicionar uma interface gráfica
- mais funções
