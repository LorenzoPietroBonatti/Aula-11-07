# 11) Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se
# # encontram o maior e o menor valor.

lista = []
for i in range(5):
    valores = float(input("Insira os valores: "))
    lista.append(valores)

###

maior_valor = max(lista)
menor_valor = min(lista)

print(maior_valor)
print(menor_valor)

posição_maior = lista.index(maior_valor)
posição_menor = lista.index(menor_valor)


print(posição_menor)
print(posição_maior)
