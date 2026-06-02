# TRABALHO AVALIATIVO – RA03
## Complexidade de Algoritmos

**Instituição:** Pontifícia Universidade Católica do Paraná  
**Escola:** Escola Politécnica  
**Curso:** Bacharelado em Ciência da Computação – 5º Período

| Campo | Informação |
|---|---|
| Disciplina | Complexidade de Algoritmos |
| Professor | Edson Emilio Scalabrin |
| Data de Entrega | 22/06/2026 |
| Tamanho da Equipe | Até 5 integrantes |
| Peso na Avaliação | 100% da nota do RA03 |

---

## 1. Definição do Problema

Considere o universo:

```
U = {1, 2, 3, ..., 25}
```

e seja

```
S_p = { X ⊆ U | |X| = p }
```

o conjunto de todas as combinações de tamanho p.

Os respectivos tamanhos dos conjuntos são:

| Conjunto | Fórmula | Cardinalidade |
|---|---|---|
| \|S₁₅\| | C(25,15) | 3.268.760 |
| \|S₁₄\| | C(25,14) | 4.457.400 |
| \|S₁₃\| | C(25,13) | 5.200.300 |
| \|S₁₂\| | C(25,12) | 5.200.300 |
| \|S₁₁\| | C(25,11) | 4.457.400 |

onde o número de combinações de p elementos dentre n é dado por:

```
C(n, p) = n! / ( p! × (n-p)! )
```

---

## 2. Atividades Propostas

### PROGRAMA 1 – Geração das Combinações

Desenvolver um algoritmo capaz de gerar integralmente os conjuntos S₁₅, S₁₄, S₁₃, S₁₂ e S₁₁, contendo todas as combinações possíveis dos elementos de U.

---

### PROGRAMA 2 – Cobertura de Combinações de 14 Elementos

Determinar um subconjunto SB₁₅,₁₄ ⊆ S₁₅ tal que toda combinação de 14 elementos esteja contida em pelo menos uma combinação de 15 elementos pertencente a SB₁₅,₁₄:

```
∀ Y ∈ S₁₄  ∃ X ∈ SB₁₅,₁₄  tal que  Y ⊆ X
```

---

### PROGRAMA 3 – Cobertura de Combinações de 13 Elementos

Determinar um subconjunto SB₁₅,₁₃ ⊆ S₁₅ tal que toda combinação de 13 elementos esteja contida em pelo menos uma combinação de 15 elementos pertencente a SB₁₅,₁₃:

```
∀ Y ∈ S₁₃  ∃ X ∈ SB₁₅,₁₃  tal que  Y ⊆ X
```

---

### PROGRAMA 4 – Cobertura de Combinações de 12 Elementos

Determinar um subconjunto SB₁₅,₁₂ ⊆ S₁₅ tal que toda combinação de 12 elementos esteja contida em pelo menos uma combinação de 15 elementos pertencente a SB₁₅,₁₂:

```
∀ Y ∈ S₁₂  ∃ X ∈ SB₁₅,₁₂  tal que  Y ⊆ X
```

---

### PROGRAMA 5 – Cobertura de Combinações de 11 Elementos

Determinar um subconjunto SB₁₅,₁₁ ⊆ S₁₅ tal que toda combinação de 11 elementos esteja contida em pelo menos uma combinação de 15 elementos pertencente a SB₁₅,₁₁:

```
∀ Y ∈ S₁₁  ∃ X ∈ SB₁₅,₁₁  tal que  Y ⊆ X
```

---

## 3. Análise de Complexidade

Para cada algoritmo desenvolvido nos Programas 2, 3, 4 e 5, realizar:

- Análise de complexidade de tempo;
- Análise de complexidade de espaço;
- Identificação dos principais gargalos computacionais;
- Discussão sobre a escalabilidade da solução proposta;
- Comparação entre diferentes estratégias de resolução, quando aplicável.

A análise deverá utilizar notação assintótica sempre que pertinente:

```
O(·)    Θ(·)    Ω(·)
```

---

## 4. Apresentação e Defesa

Cada equipe terá:

- 10 minutos para apresentação do projeto;
- 5 minutos para arguição e perguntas do professor.

A apresentação deverá contemplar:

1. Modelagem do problema;
2. Estratégia algorítmica adotada;
3. Estruturas de dados utilizadas;
4. Resultados obtidos;
5. Análise de complexidade;
6. Limitações e possíveis melhorias.

---

## 5. Critérios Importantes

Todos os integrantes da equipe deverão dominar integralmente o projeto. Durante a defesa, qualquer integrante poderá ser questionado sobre qualquer parte do trabalho, independentemente da divisão interna das atividades.

A avaliação considerará:

- Correção da solução proposta
- Qualidade da implementação
- Fundamentação teórica
- Qualidade da análise de complexidade
- Clareza da apresentação
- Capacidade de argumentação durante a defesa

---

## 6. Desafio Adicional

A abordagem por força bruta pode apresentar custo computacional extremamente elevado devido ao tamanho do espaço de busca. Assim, recomenda-se que as equipes investiguem alternativas capazes de reduzir a complexidade computacional do problema, tais como:

- Algoritmos Gulosos (Greedy)
- Branch and Bound
- Programação Inteira
- Algoritmos Probabilísticos
- Algoritmos Randômicos
- Metaheurísticas
- Computação Paralela ou Distribuída
- Outras abordagens inovadoras fundamentadas na literatura científica

**Soluções que demonstrem ganhos significativos de desempenho, devidamente justificados, serão valorizadas na avaliação.**
