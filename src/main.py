import sys
from PySide6.QtWidgets import QApplication
from controllers.viagem_controller import ViagemController

def main():
    app = QApplication(sys.argv)
    
    # Criando e iniciando o controller
    controller = ViagemController()
    controller.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 