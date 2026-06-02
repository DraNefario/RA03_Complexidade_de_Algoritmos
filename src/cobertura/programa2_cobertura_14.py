from time import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from guloso import cobertura_gulosa_pivo
from geracao.programa1_geracao import gerar_combinacoes

if __name__ == "__main__":
    print("=" * 60)
    print("PROGRAMA 2: COBERTURA EFICIENTE DE COMBINAÇÕES (MÉTODO PIVÔ)")
    print("=" * 60)
    
    
    print("\n1. Gerando apenas S14...")
    S14 = gerar_combinacoes(14)
    print(f"   S14: {len(S14):,} combinações")
    
    print("\n2. Executando cobertura por pivô...")
    inicio = time()
    cobertura, iteracoes = cobertura_gulosa_pivo(S14, t_menor=14, t_maior=15, verbose=True)
    tempo = time() - inicio
    
    print(f"\n✓ Cobertura encontrada em tempo recorde!")
    print(f"   Tamanho final de SB15,14: {len(cobertura):,} combinações")
    print(f"   Iterações: {iteracoes}")
    print(f"   Tempo de Execução: {tempo:.2f} segundos")