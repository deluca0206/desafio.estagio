import json

from desafio2 import resultado

def cacular_faturamento(dados_fat):
    faturamento_valid = [dia["faturamento"] for dia in dados_faturamento if dia ["faturamento"] > 0]

    if not faturamento_valid:
        return "Não há dados de faturamento validos."

    menor_faturamento = min(faturamento_valid)
    maior_faturamento = max(faturamento_valid)

    medio_mensal = sum(faturamento_valid) / len(faturamento_valid)

    dias_acima_da_media = len([dia for dia in faturamento_valid if dia > medio_mensal])

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

#não consegui fazer esse parte funcionar, perdão!
def ler_faturamento_arquivo(faturamento.json):
    with open(faturamento.json, "r") as arquivo:
        dados_faturamento = ler_faturamento_arquivo(faturamento.json)
    return dados_faturamento
print(dados_faturamento)


print(f"Menor Faturamento: {resultado["menor_faturamento"]}")
print(f"Maior Faturamento: {resultado["maior_faturmento"]}")
print(f"Dias com faturamento aciman da média : {resultado["dias_acima_da_media"]})