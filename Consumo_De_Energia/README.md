# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)
![Platform](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux%20%7C%20macOS-0ea5e9?style=for-the-badge&logo=linux&logoColor=white)
![Energy](https://img.shields.io/badge/Energia-kWh-facc15?style=for-the-badge&logo=lightning&logoColor=white)

---

## 📋 Sobre o projeto

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em **Python** tem a função de estimar o quanto um aparelho doméstico consome de energia elétrica por mês — e quanto ele representa na conta de luz.

você deve informar o nome do aparelho, sua potência em watts e o tempo médio de uso diário. O programa irá calcular o consumo mensal em quilowatts-hora (kWh) e o custo estimado em reais (R$), usando o preço do kWh da cidade informado pelo próprio usuário ou uma média como referência.

O projeto foi desenvolvido inteiramente com a **biblioteca padrão do Python**, sem necessidade de instalar pacotes externos.

---

## 🐍 Linguagem

Este projeto foi desenvolvido em **Python 3.6+**, utilizando apenas módulos nativos da linguagem:

| Módulo | Uso |
|--------|-----|
| `os` | Limpeza do terminal entre as telas |
| `time` | Delays e animação de carregamento |
| `datetime` | Registro da data e hora ao salvar |
| `pathlib` | Localização do arquivo de saída |

---

## 🔢 Fórmula utilizada

essa é fórmula padrão de consumo elétrico:

```
Consumo (kWh) = (Potência (W) × Horas de uso por dia × Dias no mês) ÷ 1000

Custo (R$) = Consumo (kWh) × Preço do kWh
```

**Exemplo:**
- Aparelho de 1500 W, usado 8h/dia, com kWh a R$ 0,85:
- Consumo = (1500 × 8 × 30) ÷ 1000 = **360 kWh/mês**
- Custo = 360 × 0,85 = **R$ 306,00/mês**

---

### Durante a execução

O programa irá pedir:

- 🏷️ **Nome** do aparelho
- ⚡ **Potência** em watts (W)
- 🕐 **Tempo de uso** por dia em horas
- 💰 **Preço do kWh** da sua cidade *(pode deixar em branco para usar R$ 0,75)*

No final, o resultado é exibido na tela e você pode optar por **salvar os dados** em um arquivo `.txt` ou **calcular outro aparelho**.

---

## 💾 Arquivo de saída

Ao escolher salvar, os dados serão gravados em um arquivo chamado `Dados Salvos.txt` na mesma pasta do script:

```
Data: 18/03/26 14:32:10
Aparelho: Ar-condicionado
Consumo: 360.00 kWh/mês
Preço estimado: R$306.00
```
---
