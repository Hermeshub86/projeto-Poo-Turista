from datetime import datetime
from modelo.turista import Turista
from repositorio.repositorio_memoria import RepositorioTuristaMemoria
from servico.cadastro import CadastroTurista
from visualizacao.visualizador import VisualizadorTurista

def main():
    repo = RepositorioTuristaMemoria()
    cadastro = CadastroTurista(repo)
    visualizador = VisualizadorTurista()

    turista1 = Turista("Hermes", "PB", datetime(2025, 8, 18), "Ônibus")
    cadastro.cadastrar(turista1)

    turista2 = Turista("Joana", "SP", datetime(2025, 8, 20), "Avião")
    cadastro.cadastrar(turista2)

    for t in repo.listar():
        visualizador.exibir(t)

if __name__ == "__main__":
    main()
