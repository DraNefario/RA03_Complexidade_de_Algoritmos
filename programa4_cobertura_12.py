from time import time
from guloso import cobertura_gulosa_pivo

if __name__ == "__main__":
    print("=" * 60)
    print("PROGRAMA 4: COBERTURA EFICIENTE DE COMBINAÇÕES (MÉTODO PIVÔ)")
    print("=" * 60)
    
    from programa1_geracao import gerar_combinacoes
    
    print("\n1. Gerando apenas S12...")
    S12 = gerar_combinacoes(12)
    print(f"   S12: {len(S12):,} combinações")
    
    print("\n2. Executando cobertura por pivô...")
    inicio = time()
    cobertura, iteracoes = cobertura_gulosa_pivo(S12, t_menor=12, t_maior=15, verbose=True)
    tempo = time() - inicio
    
    print(f"\n✓ Cobertura encontrada em tempo recorde!")
    print(f"   Tamanho final de SB15,12: {len(cobertura):,} combinações")
    print(f"   Iterações: {iteracoes}")
    print(f"   Tempo de Execução: {tempo:.2f} segundos")