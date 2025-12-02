"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""
from pathlib import Path
import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    """
    # Args:
    # caminho_arquivo: caminho para o CSV
    BASE_DIR = Path(__file__).parent.parent 
    caminho_arquivo = BASE_DIR/"data"/"clientes_campanha.csv"

    # Returns:
    #     DataFrame com os dados
    
    # TODO 1: Use pd.read_csv() para carregar o arquivo
    # Dica: df = pd.read_csv(caminho_arquivo)
    
    df = pd.read_csv(caminho_arquivo)
    return df

def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print("=" * 50)
    print("EXPLORAÇÃO DOS DADOS")
    print("=" * 50)
    
    # TODO 2: Mostre o shape do DataFrame (linhas, colunas)
    # Dica: print(f"Shape: {df.shape}")
    print(f"Shape: {df.shape}")
    print(f"O arquivo tem {df.shape[0]:,} linhas")
    print(f"O arquivo tem {df.shape[1]:,} colunas")
    
    print()
    # TODO 3: Mostre os tipos de cada coluna
    # Dica: print(df.dtypes)
    print("-" * 50)
    print("Tipo de dados das colunas:")
    print("-" * 50)
    print(df.dtypes)


    print()
    # TODO 4: Mostre as 5 primeiras linhas
    # Dica: print(df.head())
    
    print("-" * 50)
    print("5 primeiras linhas:")
    print("-" * 50)
    print(df.head())


    print("=" * 50)


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("\nDISTRIBUIÇÃO DO TARGET")
    print("-" * 50)
    
    # TODO 5: Mostre a contagem de cada valor do target
    # Dica: print(df[coluna_target].value_counts())
    print("Contagem de cada valor se respondeu ou não respondeu a campanha;")
    print(df[coluna_target].value_counts())
    print()
    print(f"Quantidade que respondeu a campanha: {df[coluna_target].value_counts().get(1, 0):,}")
    print(f"Quantidade que não respondeu a campanha: {df[coluna_target].value_counts().get(0, 0):,}")
    
    # TODO 6: Mostre a proporção (percentual) de cada valor
    # Dica: print(df[coluna_target].value_counts(normalize=True))
    
    print("\nProporção de cada valor do target (%):")
    print(df[coluna_target].value_counts(normalize=True)*100)
    
    print("-" * 50)


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
