numeros = set ()

for i in range(15):
    numero = int(input ('Informe o numero inteiro: '))
    numeros.add(numero)

ordenada = sorted (numeros)
print(f'Lista Ordenada: {ordenada}')