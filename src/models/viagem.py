class Viagem:
    def __init__(self, distancia: float = 0, consumo: float = 0, 
                 preco_combustivel: float = 0, pedagios: float = 0):
        self.distancia = distancia
        self.consumo = consumo
        self.preco_combustivel = preco_combustivel
        self.pedagios = pedagios

    def calcular_custo_combustivel(self) -> float:
        if self.consumo == 0:
            raise ValueError("Consumo não pode ser zero")
        litros_necessarios = self.distancia / self.consumo
        return litros_necessarios * self.preco_combustivel

    def calcular_custo_total(self) -> dict:
        custo_combustivel = self.calcular_custo_combustivel()
        custo_total = custo_combustivel + self.pedagios
        
        return {
            "custo_total": custo_total,
            "custo_combustivel": custo_combustivel,
            "custo_pedagios": self.pedagios
        } 