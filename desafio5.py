def inverter_string(s):
    lista_caracteres = list(s)
    
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    while inicio < fim:
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        inicio += 1
        fim -= 1
    
    return ''.join(lista_caracteres)

string_original = input("Digite a string que deseja inverter: ")  # Entrada do usuário
string_invertida = inverter_string(string_original)

print(f"String invertida: {string_invertida}")
