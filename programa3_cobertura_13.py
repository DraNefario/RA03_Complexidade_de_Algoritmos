from time import time
from guloso import cobertura_gulosa_pivo

if __name__ == "__main__":
    print("=" * 60)
    print("PROGRAMA 3: COBERTURA EFICIENTE DE COMBINAÇÕES (MÉTODO PIVÔ)")
    print("=" * 60)
    
    from programa1_geracao import gerar_combinacoes
    
    print("\n1. Gerando apenas S13...")
    S13 = gerar_combinacoes(13)
    print(f"   S13: {len(S13):,} combinações")
    
    print("\n2. Executando cobertura por pivô...")
    inicio = time()
    cobertura, iteracoes = cobertura_gulosa_pivo(S13, t_menor=13, t_maior=15, verbose=True)
    tempo = time() - inicio
    
    print(f"\n✓ Cobertura encontrada em tempo recorde!")
    print(f"   Tamanho final de SB15,13: {len(cobertura):,} combinações")
    print(f"   Iterações: {iteracoes}")
    print(f"   Tempo de Execução: {tempo:.2f} segundos")