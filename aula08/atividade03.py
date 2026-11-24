numeros = []


for i in range(12):
    numero = int(input ('Informe o numero inteiro: '))
    numeros.append(numero)



ordenada = sorted (numeros)
print(f'Lista Ordenada: {ordenada}')