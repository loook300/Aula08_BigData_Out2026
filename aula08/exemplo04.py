#sets "conjuntos"
#Coleção mutável
#nao garante ordem
# nao há indice 
# nao permite elementos duplicados

#Criat setes vazios 

dias = set ()

dias.add ('segunda')
dias.add('terça')
print(dias)

#conjuntos inicializados
frutas = {'maça','Uva' ,'pera','laranja'}
print (frutas)
print(type(frutas))

#remover
frutas.remove('Uva')
print(frutas)

# converter lista para sets

#lista =  [5,7,4,1,2,8,13,6]
#conjunto_set = set (lista)
#print (conjunto_set)

numeros =  [5,7,4,1,2,8,13,6,5,513,8,29]
conjunto = set (numeros)#converter lista para sets
numeros = list (conjunto) #converter conjunto set para lista
print (len(conjunto))
print(conjunto)

