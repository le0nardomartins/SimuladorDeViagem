@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo Verificando instalação do Python...
python --version > nul 2>&1
if errorlevel 1 (
    echo Python não encontrado no sistema!
    echo Por favor, instale o Python 3.8 ou superior visitando:
    echo https://www.python.org/downloads/
    echo.
    echo Pressione qualquer tecla para abrir o site de download...
    pause > nul
    start https://www.python.org/downloads/
    exit /b 1
)

echo Python encontrado! Verificando dependências...

:: Criando ambiente virtual se não existir
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

:: Ativando ambiente virtual
call venv\Scripts\activate.bat

:: Instalando/atualizando pip
python -m pip install --upgrade pip

:: Instalando dependências
echo Instalando dependências necessárias...
pip install -r requirements.txt

:: Instalando o pacote em modo de desenvolvimento
pip install -e .

:: Executando o programa
echo.
echo Iniciando o Simulador de Custo de Viagem...
echo.
python src/main.py

:: Desativando ambiente virtual
deactivate

echo.
pause 