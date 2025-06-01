from src.models.viagem import Viagem
from src.views.main_window import MainWindow

class ViagemController:
    def __init__(self):
        self.view = MainWindow()
        self.model = None
        
        # Conectando o sinal do botão calcular ao método do controller
        self.view.calcular_clicked.connect(self.calcular_viagem)
        
    def show(self):
        self.view.show()
        
    def calcular_viagem(self, dados: dict):
        try:
            # Criando uma nova instância do modelo com os dados da view
            self.model = Viagem(
                distancia=dados['distancia'],
                consumo=dados['consumo'],
                preco_combustivel=dados['preco_combustivel'],
                pedagios=dados['pedagios']
            )
            
            # Calculando o resultado
            resultados = self.model.calcular_custo_total()
            
            # Atualizando a view com os resultados
            self.view.atualizar_resultado(resultados)
            
        except ValueError as e:
            self.view.mostrar_erro(str(e))
        except Exception as e:
            self.view.mostrar_erro(f"Erro ao calcular: {str(e)}") 