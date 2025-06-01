# Simulador de Custo de Viagem

Este é um aplicativo que calcula o custo estimado de uma viagem de carro, considerando:
- Distância da viagem
- Consumo do veículo
- Preço do combustível
- Valor dos pedágios

## Modo Fácil de Execução

1. Simplesmente dê um duplo clique no arquivo `executar_simulador.bat`
2. O script vai:
   - Verificar se o Python está instalado
   - Se não estiver, fornecerá o link para download
   - Criar um ambiente virtual
   - Instalar todas as dependências necessárias
   - Iniciar o programa automaticamente

## Instalação Manual

### Requisitos
- Python 3.8 ou superior
- PySide6
- Requests

### Passos para Instalação Manual

1. Clone este repositório
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Instale o pacote em modo de desenvolvimento:
```bash
pip install -e .
```

### Execução Manual

Execute o arquivo principal:
```bash
python src/main.py
```

## Como Usar

1. Preencha os campos com as informações necessárias:
   - Distância em quilômetros
   - Consumo do veículo em km/l
   - Preço do combustível em reais
   - Valor total dos pedágios em reais

2. Clique em "Calcular Custo" para ver o resultado

## Observações

- Use ponto ou vírgula para números decimais
- Todos os campos devem ser preenchidos com valores numéricos
- O resultado mostrará o custo total da viagem, discriminando gastos com combustível e pedágios

## Problemas Comuns

1. **Python não encontrado**: 
   - Visite https://www.python.org/downloads/
   - Baixe e instale a versão mais recente
   - **Importante**: Durante a instalação, marque a opção "Add Python to PATH"

2. **Erro ao instalar dependências**:
   - Verifique sua conexão com a internet
   - Tente executar o arquivo .bat novamente
   - Se o problema persistir, tente a instalação manual