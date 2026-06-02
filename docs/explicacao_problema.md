# RA03 - Complexidade de Algoritmos: Entendendo o Problema

## 🎮 Imaginando como um Jogo de Cobertura Total

Para entender o problema sem complicações, pense nele como um desafio de "Cobertura Total" em um jogo de possibilidades.

---

## 1️⃣ O Tabuleiro (Universo $U$)

Você tem um conjunto fixo de **25 números** disponíveis:
$$U = \{1, 2, 3, \dots, 25\}$$

Esse é o seu "universo". Tudo que você faz deve usar apenas esses 25 números.

---

## 2️⃣ Os "Eventos" (O Que Você Precisa Cobrir)

Existem **4.457.400 combinações possíveis de 14 números diferentes**. 

Imagine que cada uma dessas 4,4 milhões de combinações é um **"alvo"** que você precisa atingir.

$$S_{14} = \text{Todas as combinações de 14 números de } U$$
$$|S_{14}| = \binom{25}{14} = 4.457.400$$

**Na prática:** Se alguém escolher qualquer combinação de 14 números, você precisa ter uma carta na manga para dizer: *"Eu tenho essa combinação"*.

---

## 3️⃣ As Suas "Cartas" (S₁₅)

Você tem **3.268.760 combinações de 15 números**. Essas são as suas **ferramentas de cobertura**.

$$S_{15} = \text{Todas as combinações de 15 números de } U$$
$$|S_{15}| = \binom{25}{15} = 3.268.760$$

### 🔑 A Propriedade Mágica

**Uma única combinação de 15 números contém dentro de si múltiplas combinações de 14 números.**

**Exemplo:**
- Se você tem a combinação $\{1, 2, 3, \ldots, 15\}$ de 15 números
- Você automaticamente possui as seguintes de 14 números:
  - $\{1, 2, 3, \ldots, 14\}$ (removeu o 15)
  - $\{1, 2, 3, \ldots, 13, 15\}$ (removeu o 14)
  - $\{1, 2, 3, \ldots, 13, 14\}$ (removeu o 15, deixou o 14)
  - ... e muitas outras!

**Matematicamente:** Cada combinação de 15 elementos contém exatamente $\binom{15}{14} = 15$ combinações diferentes de 14 elementos.

---

## 4️⃣ O Problema (O "X" da Questão) 🎯

**Objetivo:** Selecionar o **menor número possível** de cartas de 15 números para que, somadas, elas contenham **TODAS** as 4,4 milhões de combinações de 14 números.

**Em termos visuais:**

Imagine que você tem:
- Um **cobertor feito de 4,4 milhões de quadradinhos** (representando $S_{14}$)
- **Peças de tecido** que são um pouco maiores (representando $S_{15}$)
- Cada peça de tecido cobre vários quadradinhos (porque 15 contém múltiplos de 14)

**Seu objetivo:** Colocar essas peças de tecido sobre o cobertor de modo que **não fique nenhum buraquinho descoberto**, usando o **menor número de peças possível**.

```
Cobertor (S₁₄) com 4.457.400 quadradinhos:
┌─────────────────────────────────────────┐
│ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ... │
│ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ... │
│ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ... │
│ ... (4.457.400 quadradinhos no total)   │
└─────────────────────────────────────────┘

Peças de tecido (S₁₅) que cobrem múltiplos quadradinhos:
┌───────────────┐
│ ██████████████│  ← Cada peça cobre ~15 quadradinhos
└───────────────┘   (porque contém 15 combinações de 14)
```

---

## ❓ Por Que É Difícil?

As peças **se sobrepõem**. 

- Se você colocar uma peça, ela cobre 15 quadradinhos
- Se colocar outra, ela pode cobrir alguns quadradinhos que a primeira já cobriu
- **Isso é um desperdício!**

**O desafio é encontrar a combinação exata de peças para:**
1. ✅ Cobrir **TODOS** os quadradinhos (completude)
2. ✅ Usar o **MENOR número possível** de peças (otimalidade)

---

## 💡 A Intuição Matemática

Você pode pensar assim:

- Total de alvos (S₁₄): **4.457.400**
- Total de ferramentas (S₁₅): **3.268.760**
- Cada ferramenta cobre: **15 alvos** (em média, sem sobreposição)

**Limite teórico inferior:** $\lceil \frac{4.457.400}{15} \rceil = 297.160$ combinações de S₁₅

**Realidade:** Há sobreposição, então você **vai precisar de mais** que 297.160.

**A pergunta real é:** Quanto mais? 300 mil? 500 mil? 1 milhão?

---

## 📋 Os 5 Programas do Trabalho

O trabalho pede exatamente isso **5 vezes**, com tamanhos diferentes:

| Programa | Cobrir | Com | Pergunta |
|----------|--------|-----|----------|
| **2** | $S_{14}$ (4,4M) | $S_{15}$ (3,2M) | Quantas de S₁₅ precisa? |
| **3** | $S_{13}$ (5,2M) | $S_{15}$ (3,2M) | Quantas de S₁₅ precisa? |
| **4** | $S_{12}$ (5,2M) | $S_{15}$ (3,2M) | Quantas de S₁₅ precisa? |
| **5** | $S_{11}$ (4,4M) | $S_{15}$ (3,2M) | Quantas de S₁₅ precisa? |

---

## 🔬 O Desafio Computacional

### Força Bruta Não Funciona ❌

```
Testar todas as combinações de S₁₅:
- Há 2^3.268.760 subconjuntos de S₁₅ possíveis
- Isso é mais que átomos no universo!
- Impossível em qualquer computador
```

### Então Usamos Guloso (Greedy) ✅

```
1. Enquanto houver alvos não cobertos:
2.   Testa qual ferramenta cobre MAIS alvos
3.   Escolhe essa ferramenta
4.   Remove os alvos que ela cobriu
5.   Repete
```

**Vantagem:** Rápido (consegue rodar)  
**Desvantagem:** Pode não ser ótimo (usa um pouco mais de peças que o ideal)

---

## 🎓 Resumo

Você **não está apenas testando combinações**; você está tentando:

> **"Tapar todos os 4,4 milhões de buracos do seu universo de 14 números usando o menor número possível de 'tampas' de 15 números."**

E fazer isso **4 vezes** com tamanhos diferentes (14, 13, 12, 11).

---

## 📊 Quando Você Terminar

Vai ter respostas como:

> "Para cobrir TODAS as 4.457.400 combinações de 14 elementos usando combinações de 15 elementos, você precisa de **exatamente X.XXX combinações de S₁₅**, o que reduz o espaço em YY%."

Essas respostas são **não-triviais** e revelam propriedades matemáticas profundas sobre combinações!

---

**Agora você entende o problema? Bora implementar! 🚀**