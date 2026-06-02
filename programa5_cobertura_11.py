from time import time
from guloso import cobertura_gulosa_pivo

if __name__ == "__main__":
    print("=" * 60)
    print("PROGRAMA 5: COBERTURA EFICIENTE DE COMBINAÇÕES (MÉTODO PIVÔ)")
    print("=" * 60)
    
    from programa1_geracao import gerar_combinacoes
    
    print("\n1. Gerando apenas S11...")
    S11 = gerar_combinacoes(11)
    print(f"   S11: {len(S11):,} combinações")
    
    print("\n2. Executando cobertura por pivô...")
    inicio = time()
    cobertura, iteracoes = cobertura_gulosa_pivo(S11, t_menor=11, t_maior=15, verbose=True)
    tempo = time() - inicio
    
    print(f"\n✓ Cobertura encontrada em tempo recorde!")
    print(f"   Tamanho final de SB15,11: {len(cobertura):,} combinações")
    print(f"   Iterações: {iteracoes}")
    print(f"   Tempo de Execução: {tempo:.2f} segundos")