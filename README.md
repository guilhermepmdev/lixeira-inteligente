# 🗑️ Lixeira Inteligente

Simulação de uma lixeira que separa resíduos sozinha. Uma câmera observa o que foi jogado, uma **inteligência artificial** descobre que tipo de lixo é e um **braço mecânico controlado por Arduino** leva o objeto até o compartimento correto.

Assim, a pessoa não precisa escolher entre várias lixeiras: basta jogar o item e o sistema faz a separação.

> Este projeto é uma **simulação em Python**. Não há câmera, modelo de IA nem Arduino reais. O código reproduz a lógica de cada etapa para explicar como o sistema funcionaria.

---

## Como funciona

```
Câmera  →  Inteligência Artificial  →  Sistema de decisão  →  Arduino + braço
(imagem)     (categoria + confiança)      (escolhe destino)      (descarta no lugar certo)
```

| Etapa | No projeto real | Nesta simulação |
|---|---|---|
| 📷 Câmera | Tira uma foto do objeto | Você escolhe um objeto na lista |
| 🤖 IA | Modelo de visão computacional analisa a imagem | Uma tabela devolve categoria e confiança |
| 🧠 Decisão | Usa a categoria da IA para escolher o destino | Igual ao real |
| 🦾 Arduino | Gira os servomotores até o compartimento | Mensagens no terminal simulam o movimento |

---

## Estrutura do projeto

```
├── main.py      # Programa principal: menu, fluxo completo da lixeira
├── ia.py        # Simulação da inteligência artificial (classificação)
├── arduino.py   # Simulação do Arduino e do braço mecânico
└── README.md
```

- **`main.py`** mostra o menu de objetos e executa as quatro etapas em ordem (câmera, IA, decisão, Arduino).
- **`ia.py`** contém a função `analisar_objeto(objeto)`, que recebe o nome do objeto e devolve `(categoria, confiança)`.
- **`arduino.py`** contém a função `mover_braco(categoria)`, que simula o servo motor girando até o ângulo do compartimento.

---

## Como executar

Requisitos: **Python 3.8 ou superior**. Não é preciso instalar nenhuma biblioteca.

```bash
python main.py
```

Escolha um número do menu para jogar um objeto na lixeira. Digite `0` para sair.

### Exemplo de saída

```
📷 CÂMERA
Objeto detectado: garrafa pet

🤖 INTELIGÊNCIA ARTIFICIAL
Analisando objeto...
Objeto identificado como: garrafa pet
Categoria: Reciclável
Confiança da IA: 96%

🧠 SISTEMA DE DECISÃO
Destino escolhido: Reciclável

🦾 ARDUINO
Comando recebido: levar para Reciclável
Servo motor girando para 0°...
🦾 Braço chegou ao destino.
♻️ Descartando objeto em: Reciclável
✅ Descarte concluído!
```

---

## Compartimentos da lixeira

A lixeira tem 6 compartimentos distribuídos em círculo. O braço gira até o ângulo correspondente.

| Categoria | Ângulo do braço | Exemplos |
|---|---|---|
| Reciclável (plástico) | 0° | garrafa pet, sacola plástica |
| Papel | 60° | folha de papel, jornal, caixa de papelão |
| Orgânico | 120° | banana, casca de banana, restos de comida |
| Metal | 180° | lata, lata de refrigerante |
| Vidro | 240° | garrafa de vidro, pote de vidro |
| Rejeito | 300° | guardanapo sujo, fralda |

---

## A parte da IA

### Como seria no projeto real

1. A câmera captura uma imagem do objeto.
2. Um modelo de **visão computacional** (uma rede neural treinada com milhares de fotos de lixo) analisa a imagem.
3. O modelo devolve uma **categoria** e um **nível de confiança** (em %).

### Como é na simulação

O arquivo `ia.py` usa um dicionário que associa o nome de cada objeto à categoria e à confiança:

```python
"garrafa pet": ("Reciclável", 96),
"banana": ("Orgânico", 99),
```

Se o objeto **não está no dicionário**, a IA não o reconhece. Nesse caso, ele vai para **Rejeito** com confiança aleatória entre 50% e 75%. Essa é uma decisão de segurança: na dúvida, o item não contamina a reciclagem.

---

## Como adicionar novos objetos

Em `ia.py`, acrescente uma linha no dicionário `classificacoes`:

```python
"copo de vidro": ("Vidro", 95),
```

Para que o objeto apareça no menu, inclua o nome também na lista `OBJETOS` em `main.py`:

```python
OBJETOS = [
    "garrafa pet",
    ...
    "copo de vidro",
]
```

---

## Demonstração visual

Além do terminal, existe uma versão em **HTML, CSS e JavaScript** (`lixeira-inteligente.html`) com a mesma lógica. Nela é possível clicar em cartões ou digitar um objeto e ver o braço girando até o compartimento certo. Basta abrir o arquivo no navegador.

---

## Próximos passos (projeto real)

- Trocar a tabela de `ia.py` por um modelo treinado de classificação de imagens.
- Conectar uma câmera para capturar a foto do objeto.
- Enviar o comando do Python para o Arduino pela porta serial (por exemplo, com a biblioteca `pyserial`).
- Programar o Arduino para controlar os servomotores e mover o braço até cada ângulo.
