# 8) Crie um programa que leia 6 valores inteiros pares (GARANTA QUE ELES SEJAM PARES) e, em
# seguida, mostre na tela os valores lidos na ordem inversa.

lista = []
num = 0

while num < 6:
    valor = int(input("Insira os valores: "))

    if valor % 2 == 0:
        lista.append(valor)
        num += 1

    
print(lista)

lista.reverse()

print(lista)


    
