from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                           QFrame, QMessageBox)
from PySide6.QtCore import Qt, Signal
from src.views.styles import MAIN_STYLE, TITULO_STYLE, RESULTADO_STYLE

class MainWindow(QMainWindow):
    # Sinais para comunicação com o controller
    calcular_clicked = Signal(dict)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Simulador de Custo de Viagem")
        self.setMinimumSize(600, 400)
        self.setStyleSheet(MAIN_STYLE)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)

        # Frame principal
        main_frame = QFrame()
        main_layout = QVBoxLayout(main_frame)
        layout.addWidget(main_frame)

        # Título
        titulo = QLabel("Simulador de Custo de Viagem")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet(TITULO_STYLE)
        main_layout.addWidget(titulo)

        # Campos de entrada
        self.campos = {}
        self.criar_campo_entrada(main_layout, "Distância (km):", "distancia")
        self.criar_campo_entrada(main_layout, "Consumo do veículo (km/l):", "consumo")
        self.criar_campo_entrada(main_layout, "Preço do combustível (R$):", "preco_combustivel")
        self.criar_campo_entrada(main_layout, "Valor total dos pedágios (R$):", "pedagios")

        # Botão calcular
        btn_calcular = QPushButton("Calcular Custo")
        btn_calcular.clicked.connect(self.on_calcular)
        main_layout.addWidget(btn_calcular)

        # Resultado
        self.resultado_label = QLabel("")
        self.resultado_label.setAlignment(Qt.AlignCenter)
        self.resultado_label.setStyleSheet(RESULTADO_STYLE)
        main_layout.addWidget(self.resultado_label)

    def criar_campo_entrada(self, layout, texto, nome_objeto):
        container = QWidget()
        campo_layout = QHBoxLayout(container)
        campo_layout.setContentsMargins(0, 5, 0, 5)

        label = QLabel(texto)
        campo_layout.addWidget(label)

        entrada = QLineEdit()
        entrada.setObjectName(nome_objeto)
        self.campos[nome_objeto] = entrada
        campo_layout.addWidget(entrada)

        layout.addWidget(container)

    def on_calcular(self):
        try:
            dados = {
                'distancia': float(self.campos['distancia'].text().replace(',', '.')),
                'consumo': float(self.campos['consumo'].text().replace(',', '.')),
                'preco_combustivel': float(self.campos['preco_combustivel'].text().replace(',', '.')),
                'pedagios': float(self.campos['pedagios'].text().replace(',', '.'))
            }
            self.calcular_clicked.emit(dados)
        except ValueError:
            self.mostrar_erro("Por favor, preencha todos os campos com valores numéricos válidos.")

    def mostrar_erro(self, mensagem):
        QMessageBox.warning(self, "Erro", mensagem)

    def atualizar_resultado(self, resultados: dict):
        self.resultado_label.setText(
            f"Custo total da viagem: R$ {resultados['custo_total']:.2f}\n"
            f"Combustível: R$ {resultados['custo_combustivel']:.2f}\n"
            f"Pedágios: R$ {resultados['custo_pedagios']:.2f}"
        ) 