# 4) Ler um vetor de 5 elementos. Crie um segundo vetor, com todos os elementos na ordem 
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo 
# e assim por diante. Mostre os dois vetores. 



lista_normal = []


for i in range(5):
    value = float(input("Insira os valores: "))
    lista_normal.append(value)

print(lista_normal)


lista_normal.reverse()

print(lista_normal)

