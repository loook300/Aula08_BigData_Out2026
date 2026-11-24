vendas = []


for i in range(10):
    venda = float(input ('Informe a venda realizada:  '))
    vendas.append(venda)

total = sum(vendas)
print(f'total: {total}')