# main.py
# ---------------------------------------------------------
# LIXEIRA INTELIGENTE
# ---------------------------------------------------------

import time

from ia import analisar_objeto
from arduino import mover_braco

# Objetos disponíveis para simulação
OBJETOS = [
    "garrafa pet",
    "folha de papel",
    "banana",
    "lata",
    "garrafa de vidro",
    "guardanapo sujo",
]


def mostrar_titulo():
    print("\n")
    print("=" * 60)
    print("             🗑️ LIXEIRA INTELIGENTE")
    print("=" * 60)
    print("Sistema de separação automática de resíduos")
    print("=" * 60)


def mostrar_objetos():
    print("\n📦 OBJETOS DISPONÍVEIS:\n")

    for i, objeto in enumerate(OBJETOS, start=1):
        print(f"[{i}] {objeto}")

    print("[0] Sair")


def processar_objeto(objeto):
    """
    Executa todo o processo da lixeira.
    """

    print("\n")
    print("-" * 60)

    # -----------------------------------------------------
    # ETAPA 1 — CÂMERA
    # -----------------------------------------------------

    print("📷 CÂMERA")
    print(f"Objeto detectado: {objeto}")

    time.sleep(1)

    # -----------------------------------------------------
    # ETAPA 2 — INTELIGÊNCIA ARTIFICIAL
    # -----------------------------------------------------

    print("\n🤖 INTELIGÊNCIA ARTIFICIAL")
    print("Analisando objeto...")

    time.sleep(1)

    categoria, confianca = analisar_objeto(objeto)

    print(f"Objeto identificado como: {objeto}")
    print(f"Categoria: {categoria}")
    print(f"Confiança da IA: {confianca}%")

    time.sleep(1)

    # -----------------------------------------------------
    # ETAPA 3 — DECISÃO
    # -----------------------------------------------------

    print("\n🧠 SISTEMA DE DECISÃO")
    print(f"Destino escolhido: {categoria}")

    time.sleep(1)

    # -----------------------------------------------------
    # ETAPA 4 — ARDUINO / BRAÇO
    # -----------------------------------------------------

    mover_braco(categoria)

    print("-" * 60)


def main():

    mostrar_titulo()

    while True:

        mostrar_objetos()

        try:
            escolha = int(input("\nEscolha um objeto: "))

        except ValueError:
            print("❌ Digite apenas um número.")
            continue

        if escolha == 0:
            print("\nSistema encerrado.")
            break

        if escolha < 1 or escolha > len(OBJETOS):
            print("❌ Opção inválida.")
            continue

        objeto = OBJETOS[escolha - 1]

        processar_objeto(objeto)


if __name__ == "__main__":
    main()
