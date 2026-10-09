# ia.py
# ---------------------------------------------------------
# SIMULAÇÃO DA INTELIGÊNCIA ARTIFICIAL
# ---------------------------------------------------------
#
# No projeto real, esta parte receberia uma imagem da câmera
# e utilizaria um modelo de visão computacional para descobrir
# qual é o objeto.
#
# Nesta simulação, usamos o nome do objeto como entrada.
# ---------------------------------------------------------

import random

# Categorias existentes na nossa lixeira
CATEGORIAS = {
    "plastico": "Reciclável",
    "papel": "Papel",
    "organico": "Orgânico",
    "metal": "Metal",
    "vidro": "Vidro",
    "rejeito": "Rejeito",
}


def analisar_objeto(objeto):
    """
    Simula a análise feita pela Inteligência Artificial.

    No sistema real:
        câmera -> imagem -> modelo de IA -> categoria

    Aqui:
        objeto -> classificação simulada -> categoria
    """

    objeto = objeto.lower()

    # Simulação da classificação da IA
    classificacoes = {
        "garrafa pet": ("Reciclável", 96),
        "sacola plastica": ("Reciclável", 94),
        "garrafa plastica": ("Reciclável", 97),
        "folha de papel": ("Papel", 99),
        "jornal": ("Papel", 98),
        "caixa de papelao": ("Papel", 96),
        "banana": ("Orgânico", 99),
        "casca de banana": ("Orgânico", 98),
        "restos de comida": ("Orgânico", 95),
        "lata": ("Metal", 97),
        "lata de refrigerante": ("Metal", 98),
        "garrafa de vidro": ("Vidro", 96),
        "pote de vidro": ("Vidro", 94),
        "guardanapo sujo": ("Rejeito", 91),
        "fralda": ("Rejeito", 99),
    }

    # Procura o objeto conhecido
    if objeto in classificacoes:
        categoria, confianca = classificacoes[objeto]
    else:
        # Caso a IA não conheça o objeto
        categoria = "Rejeito"
        confianca = random.randint(50, 75)

    return categoria, confianca
