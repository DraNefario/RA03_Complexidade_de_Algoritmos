from itertools import combinations


def cobertura_gulosa_pivo(S_menor, t_menor, t_maior=15, verbose=True):
    """
    Algoritmo Guloso usando a estratégia de Elemento Pivô.
    Reduz o espaço de busca de 3.2 milhões para uma escala infinitesimal.
    """
    universo = set(range(1, 26))
    # Converte para frozenset para buscas O(1) via hash
    nao_cobertos = set(frozenset(c) for c in S_menor)
    cobertura = []
    iteracoes = 0
    
    # Quantos elementos precisamos adicionar ao pivô para virar tamanho 15
    elementos_a_adicionar = t_maior - t_menor 
    
    print(f"Iniciando cobertura para S{t_menor}... {len(nao_cobertos):,} elementos pendentes.")
    
    while nao_cobertos:
        iteracoes += 1
        
        if verbose and iteracoes % 10000 == 0:
            print(f"  Iteração {iteracoes}: {len(nao_cobertos):,} elementos não cobertos")
        
        # 1. Pegamos um elemento qualquer que PRECISA ser coberto (O Pivô)
        pivo = next(iter(nao_cobertos))
        
        # 2. Descobrimos quem do universo está de fora desse pivô
        elementos_restantes = universo - pivo
        
        melhor_combo = None
        melhor_score = -1
        melhor_subsets_cobertos = []
        
        # 3. Testamos APENAS as combinações que englobam o nosso pivô
        # Para S14 -> S15, combinações de 11 elementos tomados 1 a 1 (Apenas 11 loops)
        # Para S13 -> S15, combinações de 12 elementos tomados 2 a 2 (Apenas 66 loops)
        for adicao in combinations(elementos_restantes, elementos_a_adicionar):
            combo_maior = pivo | frozenset(adicao)
            
            # Geramos os subconjuntos desse candidato para ver o ganho colateral
            subsets_possiveis = [frozenset(c) for c in combinations(combo_maior, t_menor)]
            subsets_cobertos = [sub for sub in subsets_possiveis if sub in nao_cobertos]
            score = len(subsets_cobertos)
            
            if score > melhor_score:
                melhor_score = score
                melhor_combo = combo_maior
                melhor_subsets_cobertos = subsets_cobertos
        
        # Aloca a melhor escolha local
        cobertura.append(melhor_combo)
        
        # Remove todos que foram surfados de carona com o pivô
        nao_cobertos.difference_update(melhor_subsets_cobertos)
        
    return cobertura, iteracoes
