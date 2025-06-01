import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                           QFrame, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

class SimuladorViagem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Custo de Viagem")
        self.setMinimumSize(600, 400)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QLabel {
                color: #2c3e50;
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: white;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)

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
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(titulo)

        # Campos de entrada
        self.criar_campo_entrada(main_layout, "Distância (km):", "distancia")
        self.criar_campo_entrada(main_layout, "Consumo do veículo (km/l):", "consumo")
        self.criar_campo_entrada(main_layout, "Preço do combustível (R$):", "preco_combustivel")
        self.criar_campo_entrada(main_layout, "Valor total dos pedágios (R$):", "pedagios")

        # Botão calcular
        btn_calcular = QPushButton("Calcular Custo")
        btn_calcular.clicked.connect(self.calcular_custo)
        main_layout.addWidget(btn_calcular)

        # Resultado
        self.resultado_label = QLabel("")
        self.resultado_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultado_label.setStyleSheet("font-size: 18px; margin-top: 20px;")
        main_layout.addWidget(self.resultado_label)

    def criar_campo_entrada(self, layout, texto, nome_objeto):
        container = QWidget()
        campo_layout = QHBoxLayout(container)
        campo_layout.setContentsMargins(0, 5, 0, 5)

        label = QLabel(texto)
        campo_layout.addWidget(label)

        entrada = QLineEdit()
        entrada.setObjectName(nome_objeto)
        campo_layout.addWidget(entrada)

        layout.addWidget(container)

    def calcular_custo(self):
        try:
            distancia = float(self.findChild(QLineEdit, "distancia").text().replace(',', '.'))
            consumo = float(self.findChild(QLineEdit, "consumo").text().replace(',', '.'))
            preco_combustivel = float(self.findChild(QLineEdit, "preco_combustivel").text().replace(',', '.'))
            pedagios = float(self.findChild(QLineEdit, "pedagios").text().replace(',', '.'))

            # Cálculo do custo
            litros_necessarios = distancia / consumo
            custo_combustivel = litros_necessarios * preco_combustivel
            custo_total = custo_combustivel + pedagios

            # Formatando o resultado
            self.resultado_label.setText(
                f"Custo total da viagem: R$ {custo_total:.2f}\n"
                f"Combustível: R$ {custo_combustivel:.2f}\n"
                f"Pedágios: R$ {pedagios:.2f}"
            )
            self.resultado_label.setStyleSheet("color: #27ae60; font-weight: bold; font-size: 18px;")

        except ValueError:
            QMessageBox.warning(
                self,
                "Erro",
                "Por favor, preencha todos os campos com valores numéricos válidos."
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimuladorViagem()
    window.show()
    sys.exit(app.exec()) 