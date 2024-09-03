import json

def calcular_faturamento(dados_faturamento):
    faturamento_validos = [dia["faturamento"] for dia in dados_faturamento if dia["faturamento"] > 0]

    if not faturamento_validos:
        return "Não há dados de faturamento válidos para calcular."

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    dias_acima_da_media = len([dia for dia in faturamento_validos if dia > media_mensal])
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }
#não consegui fazer funcionar, perdão!
def ler_faturamento_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        dados_faturamento = json.load(arquivo)
    return dados_faturamento

caminho_arquivo = "faturamento.json"
dados_faturamento = ler_faturamento_arquivo(caminho_arquivo)
resultado = calcular_faturamento(dados_faturamento)

print(f"Menor faturamento: {resultado['menor_faturamento']}")
print(f"Maior faturamento: {resultado['maior_faturamento']}")
print(f"Dias com faturamento acima da média: {resultado['dias_acima_da_media']}")
