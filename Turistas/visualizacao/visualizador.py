class VisualizadorTurista:
    def exibir(self, turista):
        print(f"Nome: {turista.nome}")
        print(f"Origem: {turista.estado_origem}")
        print(f"Chegada: {turista.data_chegada.strftime('%d/%m/%Y')}")
        print(f"Transporte: {turista.transporte}")
        print("-" * 30)
