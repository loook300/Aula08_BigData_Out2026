produtos = []

for i in range (5):
    produto = input ('Informe o nome do produto:  ')
    produtos.append(produto)


print (produtos)

#Acesso ao elemento

n = int (input("Digite o indice do elemento a acessar : "))
print (produtos [n-1])



# Alterando uma lista " nome de um elemento "
produtos [n-1] =input (f'Informe o nome do outro Produto {n}: ')
print (produtos)


#Remoção de um elemento
produto_a_remover = input('\n Digite o nome do Produto a remover: ')

if produto_a_remover in produtos: 
    produtos.remove (produto_a_remover)

print (produtos)

#Pesquisar os metodos insert , pop(), clear

