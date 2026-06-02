from itertools import combinations

U = set(range(1, 26))  # {1, 2, ..., 25}

# Gerar combinações de tamanho p
def gerar_combinacoes(p):
    return list(combinations(U, p))


if __name__ == "__main__":
    print("Gerando combinações...")

    S15 = gerar_combinacoes(15)  # 3.268.760 combinações
    S14 = gerar_combinacoes(14)  # 4.457.400 combinações
    S13 = gerar_combinacoes(13)  # 5.200.300 combinações
    S12 = gerar_combinacoes(12)  # 5.200.300 combinações
    S11 = gerar_combinacoes(11)  # 4.457.400 combinações

    print(f"S15: {len(S15):,} combinações")
    print(f"S14: {len(S14):,} combinações")
    print(f"S13: {len(S13):,} combinações")
    print(f"S12: {len(S12):,} combinações")
    print(f"S11: {len(S11):,} combinações")

"""
Análise de Complexidade do Programa 1:

Tempo: O(C(n,p)) - precisa gerar todas as combinações
Espaço: O(C(n,p)) - armazenar todas elas
"""