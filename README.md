# Simulador de Custo de Viagem

Este é um aplicativo que calcula o custo estimado de uma viagem de carro, considerando:
- Distância da viagem
- Consumo do veículo
- Preço do combustível
- Valor dos pedágios

## Requisitos

- Python 3.8 ou superior
- PyQt6
- Requests

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Execute o arquivo principal:
```bash
python src/main.py
```

2. Preencha os campos com as informações necessárias:
   - Distância em quilômetros
   - Consumo do veículo em km/l
   - Preço do combustível em reais
   - Valor total dos pedágios em reais

3. Clique em "Calcular Custo" para ver o resultado

## Observações

- Use ponto ou vírgula para números decimais
- Todos os campos devem ser preenchidos com valores numéricos
- O resultado mostrará o custo total da viagem, discriminando gastos com combustível e pedágios