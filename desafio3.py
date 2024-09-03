import json

def calcular_faturamento(dados_faturamento):
    # Filtrar os dias com faturamento maior que zero
    faturamento_validos = [dia["faturamento"] for dia in dados_faturamento if dia["faturamento"] > 0]
    
    # Se não houver faturamentos válidos, retorna mensagem
    if not faturamento_validos:
        return {"menor_faturamento": None, "maior_faturamento": None, "dias_acima_da_media": None}
    
    # Calcular menor e maior valor de faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    
    # Calcular a média mensal de faturamento
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    
    # Contar o número de dias com faturamento acima da média
    dias_acima_da_media = len([dia for dia in faturamento_validos if dia > media_mensal])
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

# Função para ler o JSON de faturamento
def ler_faturamento_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            dados_faturamento = json.load(arquivo)
        return dados_faturamento
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo não está em um formato JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Exemplo de uso
caminho_arquivo = "faturamento.json"
dados_faturamento = ler_faturamento_arquivo(caminho_arquivo)

if dados_faturamento:
    resultado = calcular_faturamento(dados_faturamento)

    # Exibir os resultados
    print(f"Menor faturamento: {resultado['menor_faturamento']}")
    print(f"Maior faturamento: {resultado['maior_faturamento']}")
    print(f"Dias com faturamento acima da média: {resultado['dias_acima_da_media']}")
