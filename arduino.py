# arduino.py
# ---------------------------------------------------------
# SIMULAÇÃO DO ARDUINO
# ---------------------------------------------------------
#
# No projeto físico, o Arduino receberia um comando e
# controlaria os servomotores responsáveis pelo movimento
# do braço mecânico.
#
# Nesta versão, apenas simulamos esse comportamento.
# ---------------------------------------------------------

import time

# Posição de cada compartimento
POSICOES = {
    "Reciclável": 0,
    "Papel": 60,
    "Orgânico": 120,
    "Metal": 180,
    "Vidro": 240,
    "Rejeito": 300,
}


def mover_braco(categoria):
    """
    Simula o Arduino movimentando o braço mecânico.
    """

    if categoria not in POSICOES:
        print("Categoria desconhecida.")
        return

    angulo = POSICOES[categoria]

    print("\n🦾 ARDUINO")
    print(f"Comando recebido: levar para {categoria}")
    print(f"Servo motor girando para {angulo}°...")

    time.sleep(1)

    print("🦾 Braço chegou ao destino.")

    time.sleep(0.5)

    print(f"♻️ Descartando objeto em: {categoria}")

    time.sleep(1)

    print("✅ Descarte concluído!")
