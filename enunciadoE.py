def inverter_string(s):
    # Converte a string em uma lista para poder modificar os caracteres
    s = list(s)
    inicio = 0
    fim = len(s) - 1

    while inicio < fim:
        # Troca os caracteres nos pontos de início e fim
        s[inicio], s[fim] = s[fim], s[inicio]
        inicio += 1
        fim -= 1

    # Converte a lista de volta para uma string
    return ''.join(s)

# Exemplo de uso
string_original = input("Digite a sua string: ")
string_invertida = inverter_string(string_original)
print(string_invertida) # Saída: "!dnomu ,álO"
