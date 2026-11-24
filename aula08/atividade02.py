numeros = []

while True:
    numero = float(input ('\nInforme o numero:  '))
    numeros.append(numero)
    resposta = input ('\n Quer continuar [S/N] ? ').upper()

    if resposta == 'N' :
        break
quantidade = len(numeros)
ordenada = sorted (numeros)

print(f'total de Numeros: {quantidade}')
print(f'Lista Ordenada: {ordenada}')